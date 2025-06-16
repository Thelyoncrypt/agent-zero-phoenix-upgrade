# python/helpers/settings_manager.py
import yaml
import os
import json
from typing import Dict, Any, Optional
from pathlib import Path
from dotenv import load_dotenv

CONFIG_DIR = Path(__file__).resolve().parent.parent.parent / "config"
DEFAULT_SETTINGS_FILE = CONFIG_DIR / "default_settings.yaml"

class SettingsManager:
    _instance = None
    _settings: Optional[Dict[str, Any]] = None
    _default_yaml_structure: Optional[Dict[str, Any]] = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SettingsManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            self._load_settings()
            self._initialized = True
    
    def _load_default_yaml_for_structure(self) -> Dict[str, Any]:
        """Loads only the default YAML for its structure, without env overrides."""
        if self._default_yaml_structure is None:
            try:
                with open(DEFAULT_SETTINGS_FILE, 'r') as f:
                    self._default_yaml_structure = yaml.safe_load(f) or {}
            except Exception as e:
                print(f"SettingsManager ERROR: Could not load default settings YAML for structure: {e}")
                self._default_yaml_structure = {}
        return self._default_yaml_structure

    def _load_settings(self):
        # 1. Load defaults from YAML
        default_settings = self._load_default_yaml_for_structure()

        # 2. Override with environment variables
        project_root = Path(__file__).resolve().parents[2]
        dotenv_path = project_root / '.env'
        if dotenv_path.exists():
            load_dotenv(dotenv_path, override=True)
        
        env_overrides = self._get_env_overrides(default_settings)
        merged_settings = self._deep_merge(default_settings, env_overrides)
        self._settings = merged_settings
        print("SettingsManager: Settings loaded and merged.")

    def _get_env_overrides(self, defaults: Dict[str, Any]) -> Dict[str, Any]:
        overrides = {}
        api_keys_config_structure = defaults.get("api_keys", {})
        loaded_api_keys = {}
        
        for key_name_in_yaml in api_keys_config_structure.keys():
            env_var_name = key_name_in_yaml.upper()
            env_value = os.getenv(env_var_name)
            if env_value:
                loaded_api_keys[key_name_in_yaml] = env_value
        
        if loaded_api_keys:
            overrides["api_keys"] = loaded_api_keys
        
        # Example for other overrides
        if os.getenv("BROWSER_AGENT_HEADLESS"):
            headless_val = os.getenv("BROWSER_AGENT_HEADLESS", "true").lower() == 'true'
            overrides["tools"] = overrides.get("tools", {})
            overrides["tools"]["browser_agent"] = overrides["tools"].get("browser_agent", {})
            overrides["tools"]["browser_agent"]["headless"] = headless_val
        
        return overrides

    def _deep_merge(self, base: Dict, overrides: Dict) -> Dict:
        merged = base.copy()
        for key, value in overrides.items():
            if isinstance(value, dict) and key in merged and isinstance(merged[key], dict):
                merged[key] = self._deep_merge(merged[key], value)
            else:
                merged[key] = value
        return merged

    def _prepare_settings_for_saving(self, settings_to_save: Dict[str, Any]) -> Dict[str, Any]:
        """Prepares settings for YAML, restoring placeholders for env-sourced API keys."""
        savable_settings = json.loads(json.dumps(settings_to_save))  # Deep copy
        
        default_yaml_api_keys = self._load_default_yaml_for_structure().get("api_keys", {})
        current_env_api_keys = self._get_env_overrides({}).get("api_keys", {})

        if "api_keys" in savable_settings:
            final_api_keys_to_save = {}
            for key_in_yaml, default_placeholder in default_yaml_api_keys.items():
                current_live_value = savable_settings["api_keys"].get(key_in_yaml)
                env_sourced_value = current_env_api_keys.get(key_in_yaml)

                if env_sourced_value and current_live_value == env_sourced_value:
                    # Value matches .env, so save the placeholder from default_settings.yaml
                    final_api_keys_to_save[key_in_yaml] = default_placeholder
                else:
                    # Value was changed by user in UI, or wasn't from .env
                    final_api_keys_to_save[key_in_yaml] = current_live_value
            savable_settings["api_keys"] = final_api_keys_to_save
        return savable_settings

    def update_settings(self, new_settings_data: Dict[str, Any]) -> bool:
        if self._settings is None:
            self._load_settings()
        
        # Perform a deep merge of new data onto current settings
        self._settings = self._deep_merge(self._settings, new_settings_data)
        
        settings_to_persist = self._prepare_settings_for_saving(self._settings)
        
        try:
            with open(DEFAULT_SETTINGS_FILE, 'w', encoding='utf-8') as f:
                yaml.dump(settings_to_persist, f, indent=2, sort_keys=False, default_flow_style=False)
            print(f"SettingsManager: Settings updated and saved to {DEFAULT_SETTINGS_FILE}.")
            return True
        except Exception as e:
            print(f"SettingsManager ERROR: Could not save updated settings to {DEFAULT_SETTINGS_FILE}: {e}")
            return False

    def get_setting(self, key_path: str, default: Any = None) -> Any:
        if self._settings is None:
            self._load_settings()
        keys = key_path.split('.')
        val = self._settings
        try:
            for key in keys:
                val = val[key]
            return val
        except (KeyError, TypeError):
            return default

    def get_all_settings(self) -> Dict[str, Any]:
        if self._settings is None:
            self._load_settings()
        return self._settings.copy()

    def get_displayable_settings(self) -> Dict[str, Any]:
        if self._settings is None:
            self._load_settings()
        displayable = json.loads(json.dumps(self._settings))
        if "api_keys" in displayable:
            for key in displayable["api_keys"]:
                val = displayable["api_keys"][key]
                if val and isinstance(val, str) and len(val) > 4:
                    displayable["api_keys"][key] = f"****{val[-4:]}"
                elif val:
                    displayable["api_keys"][key] = "****"
        return displayable

def get_settings_manager() -> SettingsManager:
    return SettingsManager()
