├── .codespellrc
├── .cursor
    ├── Dockerfile
    ├── environment.json
    └── rules
    │   ├── authorization-and-rbac.mdc
    │   ├── entitlements.mdc
    │   ├── frontend-features.mdc
    │   ├── general-info.mdc
    │   └── public-api.mdc
├── .dockerignore
├── .env.dev-azure.example
├── .env.dev.example
├── .env.prod.example
├── .eslintignore
├── .github
    ├── CODEOWNERS
    ├── DISCUSSION_TEMPLATE
    │   └── ideas.yml
    ├── ISSUE_TEMPLATE
    │   ├── bug_report.yml
    │   └── config.yml
    ├── PULL_REQUEST_TEMPLATE.md
    ├── dependabot.yml
    └── workflows
    │   ├── _deploy_ecs_service.yml
    │   ├── ci.yml.template
    │   ├── codeql.yml
    │   ├── codespell.yml
    │   ├── dependabot-rebase-stale.yml
    │   ├── deploy.yml
    │   ├── licencecheck.yml
    │   ├── pipeline.yml
    │   ├── release.yml
    │   ├── snyk.yml
    │   └── stale_issues.yml
├── .gitignore
├── .husky
    ├── pre-commit
    └── pre-push
├── .npmrc
├── .nvmrc
├── .vscode
    ├── extensions.json
    ├── launch.json
    └── settings.json
├── AGENTS.md
├── CONTRIBUTING.md
├── LICENSE
├── README.cn.md
├── README.ja.md
├── README.kr.md
├── README.md
├── SECURITY.md
├── docker-compose.build.yml
├── docker-compose.dev-azure.yml
├── docker-compose.dev.yml
├── docker-compose.yml
├── ee
    ├── .eslintrc.js
    ├── LICENSE
    ├── README.md
    ├── package.json
    ├── src
    │   ├── ee-license-check
    │   │   └── index.ts
    │   ├── env.ts
    │   └── index.ts
    └── tsconfig.json
├── fern
    ├── apis
    │   ├── client
    │   │   ├── definition
    │   │   │   ├── api.yml
    │   │   │   ├── commons.yml
    │   │   │   └── score.yml
    │   │   └── generators.yml
    │   ├── organizations
    │   │   ├── definition
    │   │   │   ├── api.yml
    │   │   │   ├── commons.yml
    │   │   │   └── organizations.yml
    │   │   └── generators.yml
    │   └── server
    │   │   ├── definition
    │   │       ├── annotation-queues.yml
    │   │       ├── api.yml
    │   │       ├── comments.yml
    │   │       ├── commons.yml
    │   │       ├── dataset-items.yml
    │   │       ├── dataset-run-items.yml
    │   │       ├── datasets.yml
    │   │       ├── health.yml
    │   │       ├── ingestion.yml
    │   │       ├── media.yml
    │   │       ├── metrics.yml
    │   │       ├── models.yml
    │   │       ├── observations.yml
    │   │       ├── organizations.yml
    │   │       ├── projects.yml
    │   │       ├── prompt-version.yml
    │   │       ├── prompts.yml
    │   │       ├── scim.yml
    │   │       ├── score-configs.yml
    │   │       ├── score-v2.yml
    │   │       ├── score.yml
    │   │       ├── sessions.yml
    │   │       ├── trace.yml
    │   │       └── utils
    │   │       │   └── pagination.yml
    │   │   └── generators.yml
    └── fern.config.json
├── generated
    └── .gitignore
├── package.json
├── packages
    ├── config-eslint
    │   ├── library.js
    │   ├── next.js
    │   └── package.json
    ├── config-typescript
    │   ├── base.json
    │   ├── nextjs.json
    │   └── package.json
    └── shared
    │   ├── .eslintrc.js
    │   ├── clickhouse
    │       ├── migrations
    │       │   ├── clustered
    │       │   │   ├── 0001_traces.down.sql
    │       │   │   ├── 0001_traces.up.sql
    │       │   │   ├── 0002_observations.down.sql
    │       │   │   ├── 0002_observations.up.sql
    │       │   │   ├── 0003_scores.down.sql
    │       │   │   ├── 0003_scores.up.sql
    │       │   │   ├── 0004_drop_observations_index.down.sql
    │       │   │   ├── 0004_drop_observations_index.up.sql
    │       │   │   ├── 0005_add_session_id_index.down.sql
    │       │   │   ├── 0005_add_session_id_index.up.sql
    │       │   │   ├── 0006_add_user_id_index.down.sql
    │       │   │   ├── 0006_add_user_id_index.up.sql
    │       │   │   ├── 0007_add_event_log.down.sql
    │       │   │   ├── 0007_add_event_log.up.sql
    │       │   │   ├── 0008_add_environments_column.down.sql
    │       │   │   ├── 0008_add_environments_column.up.sql
    │       │   │   ├── 0009_add_project_environments.down.sql
    │       │   │   ├── 0009_add_project_environments.up.sql
    │       │   │   ├── 0010_add_metadata_column_on_scores.down.sql
    │       │   │   ├── 0010_add_metadata_column_on_scores.up.sql
    │       │   │   ├── 0011_add_blob_storage_file_log.down.sql
    │       │   │   ├── 0011_add_blob_storage_file_log.up.sql
    │       │   │   ├── 0012_add_session_id_column_scores.down.sql
    │       │   │   ├── 0012_add_session_id_column_scores.up.sql
    │       │   │   ├── 0013_drop_scores_trace_id_index.down.sql
    │       │   │   ├── 0013_drop_scores_trace_id_index.up.sql
    │       │   │   ├── 0014_scores_modify_nullable_trace_id_column.down.sql
    │       │   │   ├── 0014_scores_modify_nullable_trace_id_column.up.sql
    │       │   │   ├── 0015_add_scores_trace_index.down.sql
    │       │   │   ├── 0015_add_scores_trace_index.up.sql
    │       │   │   ├── 0016_add_scores_session_index.down.sql
    │       │   │   ├── 0016_add_scores_session_index.up.sql
    │       │   │   ├── 0017_add_run_id_column_scores.down.sql
    │       │   │   ├── 0017_add_run_id_column_scores.up.sql
    │       │   │   ├── 0018_add_scores_run_index.down.sql
    │       │   │   ├── 0018_add_scores_run_index.up.sql
    │       │   │   ├── 0019_analytics_traces.down.sql
    │       │   │   ├── 0019_analytics_traces.up.sql
    │       │   │   ├── 0020_analytics_observations.down.sql
    │       │   │   ├── 0020_analytics_observations.up.sql
    │       │   │   ├── 0021_analytics_scores.down.sql
    │       │   │   └── 0021_analytics_scores.up.sql
    │       │   └── unclustered
    │       │   │   ├── 0001_traces.down.sql
    │       │   │   ├── 0001_traces.up.sql
    │       │   │   ├── 0002_observations.down.sql
    │       │   │   ├── 0002_observations.up.sql
    │       │   │   ├── 0003_scores.down.sql
    │       │   │   ├── 0003_scores.up.sql
    │       │   │   ├── 0004_drop_observations_index.down.sql
    │       │   │   ├── 0004_drop_observations_index.up.sql
    │       │   │   ├── 0005_add_session_id_index.down.sql
    │       │   │   ├── 0005_add_session_id_index.up.sql
    │       │   │   ├── 0006_add_user_id_index.down.sql
    │       │   │   ├── 0006_add_user_id_index.up.sql
    │       │   │   ├── 0007_add_event_log.down.sql
    │       │   │   ├── 0007_add_event_log.up.sql
    │       │   │   ├── 0008_add_environments_column.down.sql
    │       │   │   ├── 0008_add_environments_column.up.sql
    │       │   │   ├── 0009_add_project_environments.down.sql
    │       │   │   ├── 0009_add_project_environments.up.sql
    │       │   │   ├── 0010_add_metadata_column_on_scores.down.sql
    │       │   │   ├── 0010_add_metadata_column_on_scores.up.sql
    │       │   │   ├── 0011_add_blob_storage_file_log.down.sql
    │       │   │   ├── 0011_add_blob_storage_file_log.up.sql
    │       │   │   ├── 0012_add_session_id_column_scores.down.sql
    │       │   │   ├── 0012_add_session_id_column_scores.up.sql
    │       │   │   ├── 0013_drop_scores_trace_id_index.down.sql
    │       │   │   ├── 0013_drop_scores_trace_id_index.up.sql
    │       │   │   ├── 0014_scores_modify_nullable_trace_id_column.down.sql
    │       │   │   ├── 0014_scores_modify_nullable_trace_id_column.up.sql
    │       │   │   ├── 0015_add_scores_trace_index.down.sql
    │       │   │   ├── 0015_add_scores_trace_index.up.sql
    │       │   │   ├── 0016_add_scores_session_index.down.sql
    │       │   │   ├── 0016_add_scores_session_index.up.sql
    │       │   │   ├── 0017_add_run_id_column_scores.down.sql
    │       │   │   ├── 0017_add_run_id_column_scores.up.sql
    │       │   │   ├── 0018_add_scores_run_index.down.sql
    │       │   │   ├── 0018_add_scores_run_index.up.sql
    │       │   │   ├── 0019_analytics_traces.down.sql
    │       │   │   ├── 0019_analytics_traces.up.sql
    │       │   │   ├── 0020_analytics_observations.down.sql
    │       │   │   ├── 0020_analytics_observations.up.sql
    │       │   │   ├── 0021_analytics_scores.down.sql
    │       │   │   └── 0021_analytics_scores.up.sql
    │       └── scripts
    │       │   ├── down.sh
    │       │   ├── drop.sh
    │       │   ├── seed.ts
    │       │   └── up.sh
    │   ├── package.json
    │   ├── prisma
    │       ├── database.svg
    │       ├── generated
    │       │   └── types.ts
    │       ├── migrations
    │       │   ├── 20230518191501_init
    │       │   │   └── migration.sql
    │       │   ├── 20230518193415_add_observaionts_and_traces
    │       │   │   └── migration.sql
    │       │   ├── 20230518193521_changes
    │       │   │   └── migration.sql
    │       │   ├── 20230522092340_add_metrics_and_observation_types
    │       │   │   └── migration.sql
    │       │   ├── 20230522094431_endtime_optional
    │       │   │   └── migration.sql
    │       │   ├── 20230522131516_default_timestamp
    │       │   │   └── migration.sql
    │       │   ├── 20230523082455_rename_metrics_to_gradings
    │       │   │   └── migration.sql
    │       │   ├── 20230523084523_rename_to_score
    │       │   │   └── migration.sql
    │       │   ├── 20230529140133_user_add_pw
    │       │   │   └── migration.sql
    │       │   ├── 20230530204241_auth_api_ui
    │       │   │   └── migration.sql
    │       │   ├── 20230618125818_remove_status_from_trace
    │       │   │   └── migration.sql
    │       │   ├── 20230620181114_restructure
    │       │   │   └── migration.sql
    │       │   ├── 20230622114254_new_oservations
    │       │   │   └── migration.sql
    │       │   ├── 20230623172401_observation_add_level_and_status_message
    │       │   │   └── migration.sql
    │       │   ├── 20230626095337_external_trace_id
    │       │   │   └── migration.sql
    │       │   ├── 20230705160335_add_created_updated_timestamps
    │       │   │   └── migration.sql
    │       │   ├── 20230706195819_add_completion_start_time
    │       │   │   └── migration.sql
    │       │   ├── 20230707132314_traces_project_id_index
    │       │   │   └── migration.sql
    │       │   ├── 20230707133415_user_add_email_index
    │       │   │   └── migration.sql
    │       │   ├── 20230710105741_added_indices
    │       │   │   └── migration.sql
    │       │   ├── 20230710114928_traces_add_user_id
    │       │   │   └── migration.sql
    │       │   ├── 20230710200816_scores_add_comment
    │       │   │   └── migration.sql
    │       │   ├── 20230711104810_traces_add_index
    │       │   │   └── migration.sql
    │       │   ├── 20230711110517_memberships_add_userid_index
    │       │   │   └── migration.sql
    │       │   ├── 20230711112235_fix_indices
    │       │   │   └── migration.sql
    │       │   ├── 20230717190411_users_feature_flags
    │       │   │   └── migration.sql
    │       │   ├── 20230720162550_tokens
    │       │   │   └── migration.sql
    │       │   ├── 20230720164603_migrate_tokens
    │       │   │   └── migration.sql
    │       │   ├── 20230720172051_tokens_non_null
    │       │   │   └── migration.sql
    │       │   ├── 20230721111651_drop_usage_json
    │       │   │   └── migration.sql
    │       │   ├── 20230731162154_score_value_float
    │       │   │   └── migration.sql
    │       │   ├── 20230803093326_add_release_and_version
    │       │   │   └── migration.sql
    │       │   ├── 20230809093636_remove_foreign_keys
    │       │   │   └── migration.sql
    │       │   ├── 20230809132331_add_project_id_to_observations
    │       │   │   └── migration.sql
    │       │   ├── 20230810191452_traceid_nullable_on_observations
    │       │   │   └── migration.sql
    │       │   ├── 20230810191453_project_id_not_null
    │       │   │   └── migration.sql
    │       │   ├── 20230814184705_add_viewer_membership_role
    │       │   │   └── migration.sql
    │       │   ├── 20230901155252_add_pricings_table
    │       │   │   └── migration.sql
    │       │   ├── 20230901155336_add_pricing_data
    │       │   │   └── migration.sql
    │       │   ├── 20230907204921_add_cron_jobs_table
    │       │   │   └── migration.sql
    │       │   ├── 20230907225603_projects_updated_at
    │       │   │   └── migration.sql
    │       │   ├── 20230907225604_api_keys_publishable_to_public
    │       │   │   └── migration.sql
    │       │   ├── 20230910164603_cron_add_state
    │       │   │   └── migration.sql
    │       │   ├── 20230912115644_add_trace_public_bool
    │       │   │   └── migration.sql
    │       │   ├── 20230918180320_add_indices
    │       │   │   └── migration.sql
    │       │   ├── 20230922030325_add_observation_index
    │       │   │   └── migration.sql
    │       │   ├── 20230924232619_datasets_init
    │       │   │   └── migration.sql
    │       │   ├── 20230924232620_datasets_continued
    │       │   │   └── migration.sql
    │       │   ├── 20231004005909_add_parent_observation_id_index
    │       │   │   └── migration.sql
    │       │   ├── 20231005064433_add_release_index
    │       │   │   └── migration.sql
    │       │   ├── 20231009095917_add_ondelete_cascade
    │       │   │   └── migration.sql
    │       │   ├── 20231012161041_add_events_table
    │       │   │   └── migration.sql
    │       │   ├── 20231014131841_users_add_admin_flag
    │       │   │   └── migration.sql
    │       │   ├── 20231018130032_add_per_1000_chars_pricing
    │       │   │   └── migration.sql
    │       │   ├── 20231019094815_add_additional_secret_key_column
    │       │   │   └── migration.sql
    │       │   ├── 20231021182825_user_emails_all_lowercase
    │       │   │   └── migration.sql
    │       │   ├── 20231025153548_add_headers_to_events
    │       │   │   └── migration.sql
    │       │   ├── 20231030184329_events_add_index_on_projectid
    │       │   │   └── migration.sql
    │       │   ├── 20231104004529_scores_add_index
    │       │   │   └── migration.sql
    │       │   ├── 20231104005403_fkey_indicies
    │       │   │   └── migration.sql
    │       │   ├── 20231106213824_add_openai_models
    │       │   │   └── migration.sql
    │       │   ├── 20231110012457_observation_created_at
    │       │   │   └── migration.sql
    │       │   ├── 20231110012829_observation_created_at_index
    │       │   │   └── migration.sql
    │       │   ├── 20231112095703_observations_add_unique_constraint
    │       │   │   └── migration.sql
    │       │   ├── 20231116005353_scores_unique_id_projectid
    │       │   │   └── migration.sql
    │       │   ├── 20231119171939_cron_add_job_started_at
    │       │   │   └── migration.sql
    │       │   ├── 20231119171940_bookmarked
    │       │   │   └── migration.sql
    │       │   ├── 20231129013314_invites
    │       │   │   └── migration.sql
    │       │   ├── 20231130003317_trace_session_input_output
    │       │   │   └── migration.sql
    │       │   ├── 20231204223505_add_unit_to_observations
    │       │   │   └── migration.sql
    │       │   ├── 20231223230007_cloud_config
    │       │   │   └── migration.sql
    │       │   ├── 20231223230008_accounts_add_cols_azure_ad_auth
    │       │   │   └── migration.sql
    │       │   ├── 20231230151856_add_prompt_table
    │       │   │   └── migration.sql
    │       │   ├── 20240103135918_add_pricings
    │       │   │   └── migration.sql
    │       │   ├── 20240104210051_add_model_indices
    │       │   │   └── migration.sql
    │       │   ├── 20240104210052_add_model_indices_pricing
    │       │   │   └── migration.sql
    │       │   ├── 20240105010215_add_tags_in_traces
    │       │   │   └── migration.sql
    │       │   ├── 20240105170551_index_tags_in_traces
    │       │   │   └── migration.sql
    │       │   ├── 20240106195340_drop_dataset_status
    │       │   │   └── migration.sql
    │       │   ├── 20240111152124_add_gpt_35_pricing
    │       │   │   └── migration.sql
    │       │   ├── 20240117151938_traces_remove_unique_id_external
    │       │   │   └── migration.sql
    │       │   ├── 20240117165747_add_cost_to_observations
    │       │   │   └── migration.sql
    │       │   ├── 20240118204639_add_models_table
    │       │   │   └── migration.sql
    │       │   ├── 20240118204936_add_internal_model
    │       │   │   └── migration.sql
    │       │   ├── 20240118204937_add_observations_view
    │       │   │   └── migration.sql
    │       │   ├── 20240118235424_add_index_to_models
    │       │   │   └── migration.sql
    │       │   ├── 20240119140941_add_tokenizer_id
    │       │   │   └── migration.sql
    │       │   ├── 20240119164147_make_model_params_nullable
    │       │   │   └── migration.sql
    │       │   ├── 20240119164148_add_models
    │       │   │   └── migration.sql
    │       │   ├── 20240124140443_session_composite_key
    │       │   │   └── migration.sql
    │       │   ├── 20240124164148_correct_models
    │       │   │   └── migration.sql
    │       │   ├── 20240126184148_new_models copy
    │       │   │   └── migration.sql
    │       │   ├── 20240130100110_usage_unit_nullable
    │       │   │   └── migration.sql
    │       │   ├── 20240130160110_claude_models
    │       │   │   └── migration.sql
    │       │   ├── 20240131184148_add_finetuned_and_vertex_models
    │       │   │   └── migration.sql
    │       │   ├── 20240203184148_update_pricing
    │       │   │   └── migration.sql
    │       │   ├── 20240212175433_add_audit_log_table
    │       │   │   └── migration.sql
    │       │   ├── 20240213124148_update_openai_pricing
    │       │   │   └── migration.sql
    │       │   ├── 20240214232619_prompts_add_indicies
    │       │   │   └── migration.sql
    │       │   ├── 20240215224148_update_openai_pricing
    │       │   │   └── migration.sql
    │       │   ├── 20240215234937_fix_observations_view
    │       │   │   └── migration.sql
    │       │   ├── 20240219162415_add_prompt_config
    │       │   │   └── migration.sql
    │       │   ├── 20240226165118_add_observations_index
    │       │   │   └── migration.sql
    │       │   ├── 20240226182815_add_model_index
    │       │   │   └── migration.sql
    │       │   ├── 20240226183642_add_observations_index
    │       │   │   └── migration.sql
    │       │   ├── 20240226202040_add_observations_trace_id_project_id_start_time_idx
    │       │   │   └── migration.sql
    │       │   ├── 20240226202041_add_observations_trace_id_project_id_type_start_time_idx
    │       │   │   └── migration.sql
    │       │   ├── 20240226203642_rewrite_observations_view
    │       │   │   └── migration.sql
    │       │   ├── 20240227112101_index_prompt_id_in_observations
    │       │   │   └── migration.sql
    │       │   ├── 20240228103642_observations_view_cte
    │       │   │   └── migration.sql
    │       │   ├── 20240228123642_observations_view_fix
    │       │   │   └── migration.sql
    │       │   ├── 20240304123642_traces_view
    │       │   │   └── migration.sql
    │       │   ├── 20240304123642_traces_view_improvement
    │       │   │   └── migration.sql
    │       │   ├── 20240304222519_scores_add_index
    │       │   │   └── migration.sql
    │       │   ├── 20240305095119_add_observations_index
    │       │   │   └── migration.sql
    │       │   ├── 20240305100713_traces_add_index
    │       │   │   └── migration.sql
    │       │   ├── 20240307090110_claude_model_three
    │       │   │   └── migration.sql
    │       │   ├── 20240307185543_score_add_source_nullable
    │       │   │   └── migration.sql
    │       │   ├── 20240307185544_score_add_name_index
    │       │   │   └── migration.sql
    │       │   ├── 20240307185725_backfill_score_source
    │       │   │   └── migration.sql
    │       │   ├── 20240312195727_score_source_drop_default
    │       │   │   └── migration.sql
    │       │   ├── 20240314090110_claude_model
    │       │   │   └── migration.sql
    │       │   ├── 20240325211959_remove_example_table
    │       │   │   └── migration.sql
    │       │   ├── 20240325212245_dataset_runs_add_metadata
    │       │   │   └── migration.sql
    │       │   ├── 20240326114211_dataset_run_item_bind_to_trace
    │       │   │   └── migration.sql
    │       │   ├── 20240326114337_dataset_run_item_backfill_trace_id
    │       │   │   └── migration.sql
    │       │   ├── 20240326115136_dataset_run_item_traceid_non_null
    │       │   │   └── migration.sql
    │       │   ├── 20240326115424_dataset_run_item_index_trace
    │       │   │   └── migration.sql
    │       │   ├── 20240328065738_dataset_item_input_nullable
    │       │   │   └── migration.sql
    │       │   ├── 20240404203640_dataset_item_source_trace_id
    │       │   │   └── migration.sql
    │       │   ├── 20240404210315_dataset_add_descriptions
    │       │   │   └── migration.sql
    │       │   ├── 20240404232317_dataset_items_backfill_source_trace_id
    │       │   │   └── migration.sql
    │       │   ├── 20240405124810_prompt_to_json
    │       │   │   └── migration.sql
    │       │   ├── 20240408133037_add_objects_for_evals
    │       │   │   └── migration.sql
    │       │   ├── 20240408134328_prompt_table_add_tags
    │       │   │   └── migration.sql
    │       │   ├── 20240408134330_prompt_table_add_index_to_tags
    │       │   │   └── migration.sql
    │       │   ├── 20240411134330_model_updates
    │       │   │   └── migration.sql
    │       │   ├── 20240411194142_update_job_config_status
    │       │   │   └── migration.sql
    │       │   ├── 20240411224142_update_models
    │       │   │   └── migration.sql
    │       │   ├── 20240414203636_ee_add_sso_configs
    │       │   │   └── migration.sql
    │       │   ├── 20240415235737_index_models_model_name
    │       │   │   └── migration.sql
    │       │   ├── 20240416173813_add_internal_model_index
    │       │   │   └── migration.sql
    │       │   ├── 20240417102742_metadata_on_dataset_and_dataset_item
    │       │   │   └── migration.sql
    │       │   ├── 20240419152924_posthog_integration_settings
    │       │   │   └── migration.sql
    │       │   ├── 20240420134232_posthog_integration_created_at
    │       │   │   └── migration.sql
    │       │   ├── 20240423174013_update_models
    │       │   │   └── migration.sql
    │       │   ├── 20240423192655_add_llm_api_keys
    │       │   │   └── migration.sql
    │       │   ├── 20240424150909_add_job_execution_index
    │       │   │   └── migration.sql
    │       │   ├── 20240429124411_add_prompt_version_labels
    │       │   │   └── migration.sql
    │       │   ├── 20240429194411_add_latest_prompt_tag
    │       │   │   └── migration.sql
    │       │   ├── 20240503125742_traces_add_createdat_updatedat
    │       │   │   └── migration.sql
    │       │   ├── 20240503130335_traces_index_created_at
    │       │   │   └── migration.sql
    │       │   ├── 20240503130520_traces_index_updated_at
    │       │   │   └── migration.sql
    │       │   ├── 20240508132621_scores_add_project_id
    │       │   │   └── migration.sql
    │       │   ├── 20240508132735_scores_add_projectid_index
    │       │   │   └── migration.sql
    │       │   ├── 20240508132736_scores_backfill_project_id
    │       │   │   └── migration.sql
    │       │   ├── 20240512151529_rename_memberships_to_project_memberships
    │       │   │   └── migration.sql
    │       │   ├── 20240512155020_rename_enum_membership_role_to_project_role
    │       │   │   └── migration.sql
    │       │   ├── 20240512155021_add_pricing_gpt4o
    │       │   │   └── migration.sql
    │       │   ├── 20240512155021_scores_drop_fk_on_traces_and_observations
    │       │   │   └── migration.sql
    │       │   ├── 20240512155022_scores_non_null_and_add_fk_project_id
    │       │   │   └── migration.sql
    │       │   ├── 20240513082203_scores_unique_id_and_projectid_instead_of_id_and_traceid
    │       │   │   └── migration.sql
    │       │   ├── 20240513082204_scores_unique_id_and_projectid_instead_of_id_and_traceid_index
    │       │   │   └── migration.sql
    │       │   ├── 20240513082205_observations_view_add_time_to_first_token
    │       │   │   └── migration.sql
    │       │   ├── 20240522081254_scores_add_author_user_id
    │       │   │   └── migration.sql
    │       │   ├── 20240522095738_scores_add_author_user_id_index
    │       │   │   └── migration.sql
    │       │   ├── 20240523142425_score_config_add_table
    │       │   │   └── migration.sql
    │       │   ├── 20240523142524_scores_add_config_id_idx
    │       │   │   └── migration.sql
    │       │   ├── 20240523142610_scores_add_fk_scores_config_id
    │       │   │   └── migration.sql
    │       │   ├── 20240524154058_scores_source_enum_add_annotation
    │       │   │   └── migration.sql
    │       │   ├── 20240524156058_scores_source_backfill_annotation_for_review
    │       │   │   └── migration.sql
    │       │   ├── 20240524165931_scores_source_enum_drop_review
    │       │   │   └── migration.sql
    │       │   ├── 20240524190433_job_executions_add_fk_index_config_id
    │       │   │   └── migration.sql
    │       │   ├── 20240524190434_job_executions_add_fk_index_score_id
    │       │   │   └── migration.sql
    │       │   ├── 20240524190435_job_executions_add_fk_index_trace_id
    │       │   │   └── migration.sql
    │       │   ├── 20240524190436_job_executions_index_created_at
    │       │   │   └── migration.sql
    │       │   ├── 20240528214726_add_cursor_new_columns_observations
    │       │   │   └── migration.sql
    │       │   ├── 20240528214727_add_cursor_new_columns_scores
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_01
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_02
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_03
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_04
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_05
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_06
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_07
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_08
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_09
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_10
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_11
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_12
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_13
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_14
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_15
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_16
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_17
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_18
    │       │   │   └── migration.sql
    │       │   ├── 20240603212024_dataset_items_add_index_source_trace_id
    │       │   │   └── migration.sql
    │       │   ├── 20240604133338_scores_add_index_name
    │       │   │   └── migration.sql
    │       │   ├── 20240604133339_score_data_type_add_boolean
    │       │   │   └── migration.sql
    │       │   ├── 20240606093356_drop_unused_pricings_table
    │       │   │   └── migration.sql
    │       │   ├── 20240606133011_remove_trace_fkey_datasetrunitems
    │       │   │   └── migration.sql
    │       │   ├── 20240607090858_pricings_add_latest_gemini_models
    │       │   │   └── migration.sql
    │       │   ├── 20240607212419_model_price_anthropic_via_google_vertex
    │       │   │   └── migration.sql
    │       │   ├── 20240611105521_llm_api_keys_custom_endpoints
    │       │   │   └── migration.sql
    │       │   ├── 20240611113517_backfill_manual_score_configs
    │       │   │   └── migration.sql
    │       │   ├── 20240612101858_add_index_observations_project_id_prompt_id
    │       │   │   └── migration.sql
    │       │   ├── 20240617094803_observations_remove_prompt_fk_constraint
    │       │   │   └── migration.sql
    │       │   ├── 20240618134129_add_batch_exports_table
    │       │   │   └── migration.sql
    │       │   ├── 20240618164950_drop_observations_parent_observation_id_idx
    │       │   │   └── migration.sql
    │       │   ├── 20240618164951_drop_observations_updated_at_idx
    │       │   │   └── migration.sql
    │       │   ├── 20240618164952_drop_scores_updated_at_idx
    │       │   │   └── migration.sql
    │       │   ├── 20240618164953_drop_traces_external_id_idx
    │       │   │   └── migration.sql
    │       │   ├── 20240618164954_drop_traces_release_idx
    │       │   │   └── migration.sql
    │       │   ├── 20240618164955_drop_traces_updated_at_idx
    │       │   │   └── migration.sql
    │       │   ├── 20240618164956_create_traces_project_id_timestamp_idx
    │       │   │   └── migration.sql
    │       │   ├── 20240624133412_models_add_anthropic_3_5_sonnet
    │       │   │   └── migration.sql
    │       │   ├── 20240625103957_observations_add_calculated_cost_columns
    │       │   │   └── migration.sql
    │       │   ├── 20240625103958_fix_model_match_gpt4_vision
    │       │   │   └── migration.sql
    │       │   ├── 20240703214747_models_anthropic_aws_bedrock
    │       │   │   └── migration.sql
    │       │   ├── 20240704103900_observations_view_read_from_calculated
    │       │   │   └── migration.sql
    │       │   ├── 20240704103901_scores_make_value_optional
    │       │   │   └── migration.sql
    │       │   ├── 20240705152639_traces_view_add_created_at_updated_at
    │       │   │   └── migration.sql
    │       │   ├── 20240705154048_observation_view_add_created_at_updated_at
    │       │   │   └── migration.sql
    │       │   ├── 20240710114043_score_configs_drop_empty_categories_array_for_numeric_scores
    │       │   │   └── migration.sql
    │       │   ├── 20240710114044_add_pricing_gpt4o_mini
    │       │   │   └── migration.sql
    │       │   ├── 20240718004923_datasets_tables_add_projectid_composite_key
    │       │   │   └── migration.sql
    │       │   ├── 20240718011733_dataset_runs_add_unique_dataset_id_project_id_name copy
    │       │   │   └── migration.sql
    │       │   ├── 20240718011734_dataset_runs_drop_unique_dataset_id_name
    │       │   │   └── migration.sql
    │       │   ├── 20240718011735_observation_view_add_prompt_name_and_version
    │       │   │   └── migration.sql
    │       │   ├── 20240807111358_models_add_openai_gpt_4o_2024_08_06
    │       │   │   └── migration.sql
    │       │   ├── 20240807111359_add_organizations_main_migration
    │       │   │   └── migration.sql
    │       │   ├── 20240814223824_model_fix_text_embedding_3_large
    │       │   │   └── migration.sql
    │       │   ├── 20240814233029_dataset_items_drop_fkey_on_traces_and_observations
    │       │   │   └── migration.sql
    │       │   ├── 20240815171916_add_comments
    │       │   │   └── migration.sql
    │       │   ├── 20240913095558_models_add_openai_o1_2024-09-12
    │       │   │   └── migration.sql
    │       │   ├── 20240913185822_account_add_refresh_token_expires_in
    │       │   │   └── migration.sql
    │       │   ├── 20240917183001_remove_covered_indexes_01
    │       │   │   └── migration.sql
    │       │   ├── 20240917183002_remove_covered_indexes_02
    │       │   │   └── migration.sql
    │       │   ├── 20240917183003_remove_covered_indexes_03
    │       │   │   └── migration.sql
    │       │   ├── 20240917183004_remove_covered_indexes_04
    │       │   │   └── migration.sql
    │       │   ├── 20240917183005_remove_covered_indexes_05
    │       │   │   └── migration.sql
    │       │   ├── 20240917183006_remove_covered_indexes_06
    │       │   │   └── migration.sql
    │       │   ├── 20240917183007_remove_covered_indexes_07
    │       │   │   └── migration.sql
    │       │   ├── 20240917183008_remove_covered_indexes_08
    │       │   │   └── migration.sql
    │       │   ├── 20240917183009_remove_covered_indexes_09
    │       │   │   └── migration.sql
    │       │   ├── 20240917183010_remove_covered_indexes_10
    │       │   │   └── migration.sql
    │       │   ├── 20240917183011_remove_covered_indexes_11
    │       │   │   └── migration.sql
    │       │   ├── 20240917183012_remove_covered_indexes_12
    │       │   │   └── migration.sql
    │       │   ├── 20240917183013_remove_covered_indexes_13
    │       │   │   └── migration.sql
    │       │   ├── 20240917183014_remove_covered_indexes_14
    │       │   │   └── migration.sql
    │       │   ├── 20240917183015_remove_covered_indexes_15
    │       │   │   └── migration.sql
    │       │   ├── 20240917183016_remove_covered_indexes_16
    │       │   │   └── migration.sql
    │       │   ├── 20241009042557_auth_add_created_at_for_gitlab
    │       │   │   └── migration.sql
    │       │   ├── 20241009110720_scores_add_nullable_queue_id_column
    │       │   │   └── migration.sql
    │       │   ├── 20241009113245_add_annotation_queue
    │       │   │   └── migration.sql
    │       │   ├── 20241010120245_llm_keys_add_config
    │       │   │   └── migration.sql
    │       │   ├── 20241015110145_prompts_config_to_JSON
    │       │   │   └── migration.sql
    │       │   ├── 20241022110145_add_claude_sonnet_35
    │       │   │   └── migration.sql
    │       │   ├── 20241023110145_update_claude_sonnet_35
    │       │   │   └── migration.sql
    │       │   ├── 20241024100928_add_prices_table
    │       │   │   └── migration.sql
    │       │   ├── 20241024111800_add_background_migrations_table
    │       │   │   └── migration.sql
    │       │   ├── 20241024121500_add_generations_cost_backfill_background_migration
    │       │   │   └── migration.sql
    │       │   ├── 20241024173000_add_traces_pg_to_ch_background_migration
    │       │   │   └── migration.sql
    │       │   ├── 20241024173700_add_observations_pg_to_ch_background_migration
    │       │   │   └── migration.sql
    │       │   ├── 20241024173800_add_scores_pg_to_ch_background_migration
    │       │   │   └── migration.sql
    │       │   ├── 20241029130802_prices_drop_excess_index
    │       │   │   └── migration.sql
    │       │   ├── 20241104111600_background_migrations_add_state_column
    │       │   │   └── migration.sql
    │       │   ├── 20241105110900_add_claude_haiku_35
    │       │   │   └── migration.sql
    │       │   ├── 20241106122605_add_media_tables
    │       │   │   └── migration.sql
    │       │   ├── 20241114175010_job_executions_add_observation_dataset_item_cols
    │       │   │   └── migration.sql
    │       │   ├── 20241124115100_add_projects_deleted_at
    │       │   │   └── migration.sql
    │       │   ├── 20241125124029_add_chatgpt_4o_prices
    │       │   │   └── migration.sql
    │       │   ├── 20241206115829_remove_trace_score_observation_constraints
    │       │   │   └── migration.sql
    │       │   ├── 20250108220721_add_queue_backup_table
    │       │   │   └── migration.sql
    │       │   ├── 20250109083346_drop_trace_tracesession_fk
    │       │   │   └── migration.sql
    │       │   ├── 20250116154613_add_billing_meter_backups
    │       │   │   └── migration.sql
    │       │   ├── 20250122152102_add_llm_api_keys_extra_headers
    │       │   │   └── migration.sql
    │       │   ├── 20250123103200_add_retention_days_to_projects
    │       │   │   └── migration.sql
    │       │   ├── 20250128144418_llm_adapter_rename_google_vertex_ai
    │       │   │   └── migration.sql
    │       │   ├── 20250128163035_add_nullable_commit_message_prompts
    │       │   │   └── migration.sql
    │       │   ├── 20250204180200_add_event_log_table
    │       │   │   └── migration.sql
    │       │   ├── 20250211102600_drop_event_log_table
    │       │   │   └── migration.sql
    │       │   ├── 20250211123300_drop_events_table
    │       │   │   └── migration.sql
    │       │   ├── 20250214173309_add_timescope_to_configs
    │       │   │   └── migration.sql
    │       │   ├── 20250220141500_add_environment_to_trace_sessions
    │       │   │   └── migration.sql
    │       │   ├── 20250221143400_drop_trace_view_observation_view
    │       │   │   └── migration.sql
    │       │   ├── 20250303144044_add_prompt_dependencies_table
    │       │   │   └── migration.sql
    │       │   ├── 20250310100328_add_api_key_to_audit_log
    │       │   │   └── migration.sql
    │       │   ├── 20250321102240_drop_queue_backup_table
    │       │   │   └── migration.sql
    │       │   ├── 20250324110557_add_blobstorage_integration_table
    │       │   │   └── migration.sql
    │       │   ├── 20250326180640_add_llm_tools_and_schemas_tables
    │       │   │   └── migration.sql
    │       │   ├── 20250401122159_add_prompt_protected_labels_table
    │       │   │   └── migration.sql
    │       │   ├── 20250402142320_add_blobstorage_integration_file_type
    │       │   │   └── migration.sql
    │       │   ├── 20250403153555_membership_invitations_no_duplicates
    │       │   │   └── migration.sql
    │       │   ├── 20250409154352_add_dashboard_data_model
    │       │   │   └── migration.sql
    │       │   ├── 20250410145712_add_organization_scoped_api_keys
    │       │   │   └── migration.sql
    │       │   ├── 20250420120553_add_organization_and_project_metadata
    │       │   │   └── migration.sql
    │       │   ├── 20250517173700_add_event_log_migration_background_migration.sql
    │       │   │   └── migration.sql
    │       │   ├── 20250517273700_add_table_view_presets.sql
    │       │   │   └── migration.sql
    │       │   ├── 20250519073249_add_trace_media_media_id_index
    │       │   │   └── migration.sql
    │       │   ├── 20250519073327_add_observation_media_media_id_index
    │       │   │   └── migration.sql
    │       │   ├── 20250519093327_media_add_index_project_id_id
    │       │   │   └── migration.sql
    │       │   ├── 20250519093328_media_relax_id_uniqueness_to_project_only
    │       │   │   └── migration.sql
    │       │   ├── 20250519145128_resize_dashboard_y_axis_components
    │       │   │   └── migration.sql
    │       │   ├── 20250520123737_add_single_aggregate_chart_type
    │       │   │   └── migration.sql
    │       │   ├── 20250522140357_remove_obsolete_observation_media_index
    │       │   │   └── migration.sql
    │       │   ├── 20250523100511_add_default_eval_model_table
    │       │   │   └── migration.sql
    │       │   ├── 20250523110540_modify_nullable_cols_eval_templates
    │       │   │   └── migration.sql
    │       │   ├── 20250523120545_add_nullable_job_template_id
    │       │   │   └── migration.sql
    │       │   ├── 20250529071241_make_blobstorage_integration_credentials_optional
    │       │   │   └── migration.sql
    │       │   ├── 20250604085536_add_histogram_chart_type
    │       │   │   └── migration.sql
    │       │   └── migration_lock.toml
    │       ├── schema.prisma
    │       └── seed.ts
    │   ├── scripts
    │       ├── cleanup.sql
    │       ├── load-seed.ts
    │       └── prepareClickhouse.ts
    │   ├── src
    │       ├── constants.ts
    │       ├── db.ts
    │       ├── domain
    │       │   ├── index.ts
    │       │   ├── observations.ts
    │       │   ├── scores.ts
    │       │   ├── table-view-presets.ts
    │       │   └── traces.ts
    │       ├── encryption
    │       │   └── index.ts
    │       ├── env.ts
    │       ├── errors
    │       │   ├── ApiError.ts
    │       │   ├── BaseError.ts
    │       │   ├── ConflictError.ts
    │       │   ├── ForbiddenError.ts
    │       │   ├── InternalServerError.ts
    │       │   ├── InvalidRequestError.ts
    │       │   ├── MethodNotAllowedError.ts
    │       │   ├── NotFoundError.ts
    │       │   ├── UnauthorizedError.ts
    │       │   └── index.ts
    │       ├── features
    │       │   ├── annotation
    │       │   │   └── types.ts
    │       │   ├── batchAction
    │       │   │   └── types.ts
    │       │   ├── batchExport
    │       │   │   └── types.ts
    │       │   ├── comments
    │       │   │   └── types.ts
    │       │   ├── entitlements
    │       │   │   └── plans.ts
    │       │   ├── evals
    │       │   │   ├── types.ts
    │       │   │   └── utilities.ts
    │       │   ├── experiments
    │       │   │   └── utils.ts
    │       │   ├── prompts
    │       │   │   └── parsePromptDependencyTags.ts
    │       │   └── scores
    │       │   │   ├── index.ts
    │       │   │   ├── interfaces
    │       │   │       ├── README.md
    │       │   │       ├── api
    │       │   │       │   ├── index.ts
    │       │   │       │   ├── shared.ts
    │       │   │       │   ├── v1
    │       │   │       │   │   ├── endpoints.ts
    │       │   │       │   │   ├── schemas.ts
    │       │   │       │   │   └── validation.ts
    │       │   │       │   └── v2
    │       │   │       │   │   ├── endpoints.ts
    │       │   │       │   │   ├── schemas.ts
    │       │   │       │   │   └── validation.ts
    │       │   │       ├── application
    │       │   │       │   └── validation.ts
    │       │   │       ├── index.ts
    │       │   │       ├── ingestion
    │       │   │       │   └── validation.ts
    │       │   │       ├── shared.ts
    │       │   │       └── ui
    │       │   │       │   └── types.ts
    │       │   │   └── scoreConfigTypes.ts
    │       ├── index.ts
    │       ├── interfaces
    │       │   ├── cloudConfigSchema.ts
    │       │   ├── customLLMProviderConfigSchemas.ts
    │       │   ├── filters.ts
    │       │   ├── orderBy.ts
    │       │   ├── parseDbOrg.ts
    │       │   ├── rate-limits.ts
    │       │   ├── search.ts
    │       │   └── tableNames.ts
    │       ├── observationsTable.ts
    │       ├── server
    │       │   ├── auth
    │       │   │   ├── apiKeys.ts
    │       │   │   ├── customSsoProvider.ts
    │       │   │   ├── gitHubEnterpriseProvider.ts
    │       │   │   └── types.ts
    │       │   ├── clickhouse
    │       │   │   ├── client.ts
    │       │   │   ├── schema.ts
    │       │   │   └── schemaUtils.ts
    │       │   ├── data-deletion
    │       │   │   └── ingestionFileDeletion.ts
    │       │   ├── filterToPrisma.ts
    │       │   ├── headerPropagation.ts
    │       │   ├── index.ts
    │       │   ├── ingestion
    │       │   │   ├── processEventBatch.ts
    │       │   │   ├── types.ts
    │       │   │   └── validateAndInflateScore.ts
    │       │   ├── instrumentation
    │       │   │   ├── README.md
    │       │   │   └── index.ts
    │       │   ├── llm
    │       │   │   ├── fetchLLMCompletion.ts
    │       │   │   ├── types.ts
    │       │   │   └── utils.ts
    │       │   ├── logger.ts
    │       │   ├── orderByToPrisma.ts
    │       │   ├── queries
    │       │   │   ├── clickhouse-sql
    │       │   │   │   ├── clickhouse-filter.ts
    │       │   │   │   ├── factory.ts
    │       │   │   │   ├── orderby-factory.ts
    │       │   │   │   └── search.ts
    │       │   │   ├── createGenerationsQuery.ts
    │       │   │   ├── createSessionsAllQuery.ts
    │       │   │   ├── index.ts
    │       │   │   └── types.ts
    │       │   ├── queues.ts
    │       │   ├── redis
    │       │   │   ├── batchActionQueue.ts
    │       │   │   ├── batchExport.ts
    │       │   │   ├── blobStorageIntegrationProcessingQueue.ts
    │       │   │   ├── blobStorageIntegrationQueue.ts
    │       │   │   ├── cloudUsageMeteringQueue.ts
    │       │   │   ├── coreDataS3ExportQueue.ts
    │       │   │   ├── createEvalQueue.ts
    │       │   │   ├── dataRetentionProcessingQueue.ts
    │       │   │   ├── dataRetentionQueue.ts
    │       │   │   ├── datasetRunItemUpsert.ts
    │       │   │   ├── dlqRetryQueue.ts
    │       │   │   ├── evalExecutionQueue.ts
    │       │   │   ├── experimentCreateQueue.ts
    │       │   │   ├── getQueue.ts
    │       │   │   ├── ingestionQueue.ts
    │       │   │   ├── meteringDataPostgresExportQueue.ts
    │       │   │   ├── postHogIntegrationProcessingQueue.ts
    │       │   │   ├── postHogIntegrationQueue.ts
    │       │   │   ├── projectDelete.ts
    │       │   │   ├── redis.ts
    │       │   │   ├── scoreDelete.ts
    │       │   │   ├── traceDelete.ts
    │       │   │   └── traceUpsert.ts
    │       │   ├── repositories
    │       │   │   ├── README.md
    │       │   │   ├── blobStorageLog.ts
    │       │   │   ├── clickhouse.ts
    │       │   │   ├── constants.ts
    │       │   │   ├── dashboards.ts
    │       │   │   ├── definitions.ts
    │       │   │   ├── environments.ts
    │       │   │   ├── index.ts
    │       │   │   ├── observations.ts
    │       │   │   ├── observations_converters.ts
    │       │   │   ├── scores-utils.ts
    │       │   │   ├── scores.ts
    │       │   │   ├── scores_converters.ts
    │       │   │   ├── trace-sessions.ts
    │       │   │   ├── traces.ts
    │       │   │   ├── traces_converters.ts
    │       │   │   └── types.ts
    │       │   ├── s3
    │       │   │   └── index.ts
    │       │   ├── services
    │       │   │   ├── DashboardService
    │       │   │   │   ├── DashboardService.ts
    │       │   │   │   ├── index.ts
    │       │   │   │   └── types.ts
    │       │   │   ├── DefaultEvaluationModelService
    │       │   │   │   ├── DefaultEvalModelService.ts
    │       │   │   │   └── index.ts
    │       │   │   ├── PromptService
    │       │   │   │   ├── index.ts
    │       │   │   │   ├── types.ts
    │       │   │   │   └── utils.ts
    │       │   │   ├── StorageService.ts
    │       │   │   ├── TableViewService
    │       │   │   │   ├── TableViewService.ts
    │       │   │   │   ├── index.ts
    │       │   │   │   └── types.ts
    │       │   │   ├── datasets-ui-table-service.ts
    │       │   │   ├── email
    │       │   │   │   ├── batchExportSuccess
    │       │   │   │   │   ├── BatchExportSuccessEmailTemplate.tsx
    │       │   │   │   │   └── sendBatchExportSuccessEmail.ts
    │       │   │   │   ├── organizationInvitation
    │       │   │   │   │   ├── MembershipInvitationEmailTemplate.tsx
    │       │   │   │   │   └── sendMembershipInvitationEmail.ts
    │       │   │   │   └── passwordReset
    │       │   │   │   │   └── sendResetPasswordVerificationRequest.tsx
    │       │   │   ├── sessions-ui-table-service.ts
    │       │   │   └── traces-ui-table-service.ts
    │       │   ├── test-utils
    │       │   │   ├── clickhouse-helpers.ts
    │       │   │   ├── index.ts
    │       │   │   ├── org-factory.ts
    │       │   │   └── tracing-factory.ts
    │       │   └── utils
    │       │   │   ├── DatabaseReadStream.ts
    │       │   │   ├── metadata_conversion.ts
    │       │   │   └── transforms
    │       │   │       ├── index.ts
    │       │   │       ├── stringify.ts
    │       │   │       ├── transformStreamToCsv.ts
    │       │   │       ├── transformStreamToJson.ts
    │       │   │       └── transformStreamToJsonl.ts
    │       ├── tableDefinitions
    │       │   ├── index.ts
    │       │   ├── mapDashboards.ts
    │       │   ├── mapObservationsTable.ts
    │       │   ├── mapScoresTable.ts
    │       │   ├── mapSessionTable.ts
    │       │   ├── mapTracesTable.ts
    │       │   ├── sessionsView.ts
    │       │   ├── tracesTable.ts
    │       │   ├── typeHelpers.ts
    │       │   └── types.ts
    │       ├── types.ts
    │       └── utils
    │       │   ├── environment.ts
    │       │   ├── json.ts
    │       │   ├── objects.ts
    │       │   ├── scores.ts
    │       │   ├── stringChecks.ts
    │       │   ├── typeChecks.ts
    │       │   └── zod.ts
    │   └── tsconfig.json
├── patches
    └── next-auth@4.24.11.patch
├── pnpm-lock.yaml
├── pnpm-workspace.yaml
├── scripts
    └── nuke.sh
├── turbo.json
├── web
    ├── .eslintrc.js
    ├── Dockerfile
    ├── components.json
    ├── entrypoint.sh
    ├── jest.config.mjs
    ├── next.config.mjs
    ├── package.json
    ├── playwright.config.ts
    ├── postcss.config.cjs
    ├── prettier.config.cjs
    ├── public
    │   ├── android-chrome-192x192.png
    │   ├── apple-touch-icon.png
    │   ├── assets
    │   │   ├── huggingface-logo.svg
    │   │   └── ragas-logo.png
    │   ├── favicon-16x16.png
    │   ├── favicon-32x32.png
    │   ├── favicon.ico
    │   ├── generated
    │   │   ├── api-client
    │   │   │   └── openapi.yml
    │   │   ├── api
    │   │   │   └── openapi.yml
    │   │   ├── organizations-api
    │   │   │   └── openapi.yml
    │   │   ├── organizations-postman
    │   │   │   └── collection.json
    │   │   └── postman
    │   │   │   └── collection.json
    │   ├── icon.svg
    │   └── icon256.png
    ├── sentry.client.config.ts
    ├── src
    │   ├── __e2e__
    │   │   ├── api.servertest.ts
    │   │   ├── auth.spec.ts
    │   │   └── create-project.spec.ts
    │   ├── __tests__
    │   │   ├── after-teardown.ts
    │   │   ├── aggregateScores.clienttest.ts
    │   │   ├── annotation-queues-api.servertest.ts
    │   │   ├── api-auth.servertest.ts
    │   │   ├── async
    │   │   │   ├── comments-api.servertest.ts
    │   │   │   ├── daily-metrics-api.servertest.ts
    │   │   │   ├── dataset-service.servertest.ts
    │   │   │   ├── datasets-api.servertest.ts
    │   │   │   ├── datasets-ui-table.servertest.ts
    │   │   │   ├── evals-trpc.servertest.ts
    │   │   │   ├── ingestion-api.servertest.ts
    │   │   │   ├── memberships-api.servertest.ts
    │   │   │   ├── metrics-api.servertest.ts
    │   │   │   ├── observation-api.servertest.ts
    │   │   │   ├── organizations-api-key-trpc.servertest.ts
    │   │   │   ├── organizations-api.servertest.ts
    │   │   │   ├── projects-api.servertest.ts
    │   │   │   ├── repositories
    │   │   │   │   ├── dashboard-repository.servertest.ts
    │   │   │   │   ├── environment-repository.servertest.ts
    │   │   │   │   ├── observation-repository.servertest.ts
    │   │   │   │   ├── score-repository.servertest.ts
    │   │   │   │   └── trace-repository.servertest.ts
    │   │   │   ├── scim-api.servertest.ts
    │   │   │   ├── scores-api-v1.servertest.ts
    │   │   │   ├── scores-api-v2.servertest.ts
    │   │   │   ├── scores-trpc.servertest.ts
    │   │   │   ├── sessions-api.servertest.ts
    │   │   │   ├── sessions-trpc.servertest.ts
    │   │   │   ├── sessions-ui-table.servertest.ts
    │   │   │   ├── traces-api.servertest.ts
    │   │   │   ├── traces-trpc.servertest.ts
    │   │   │   ├── traces-ui-table.servertest.ts
    │   │   │   └── users-ui-table.servertest.ts
    │   │   ├── dom.clienttest.ts
    │   │   ├── fixtures
    │   │   │   └── TestRouter.ts
    │   │   ├── ingestion-unit.servertest.ts
    │   │   ├── llm-api-key.servertest.ts
    │   │   ├── markdown.clienttest.ts
    │   │   ├── media.servertest.ts
    │   │   ├── model-definitions.servertest.ts
    │   │   ├── orderByToPrisma.servertest.ts
    │   │   ├── promptCache.servertest.ts
    │   │   ├── prompts.v1.servertest.ts
    │   │   ├── prompts.v2.servertest.ts
    │   │   ├── queryBuilder.servertest.ts
    │   │   ├── queryBuilderDashboards.servertest.ts
    │   │   ├── queryBuilderSQLI.servertest.ts
    │   │   ├── rate-limit.servertest.ts
    │   │   ├── score-configs.servertest.ts
    │   │   ├── server
    │   │   │   └── api
    │   │   │   │   ├── otel
    │   │   │   │       └── otelMapping.servertest.ts
    │   │   │   │   └── tables
    │   │   │   │       └── prompts-ui.servertest.ts
    │   │   ├── sessions.servertest.ts
    │   │   ├── static
    │   │   │   ├── bitcoin.pdf
    │   │   │   └── langfuse-logo.png
    │   │   ├── table-view-presets.clienttest.ts
    │   │   ├── teardown.ts
    │   │   ├── test-utils.ts
    │   │   └── zod.servertest.ts
    │   ├── app
    │   │   ├── api
    │   │   │   ├── billing
    │   │   │   │   └── stripe-webhook
    │   │   │   │   │   └── route.ts
    │   │   │   └── chatCompletion
    │   │   │   │   └── route.ts
    │   │   └── layout.tsx
    │   ├── components
    │   │   ├── ActionButton.tsx
    │   │   ├── BatchExportTableButton.tsx
    │   │   ├── ChatMessages
    │   │   │   ├── ChatMessageComponent.tsx
    │   │   │   ├── ToolCallCard.tsx
    │   │   │   ├── index.tsx
    │   │   │   ├── types.ts
    │   │   │   └── utils
    │   │   │   │   └── createEmptyMessage.ts
    │   │   ├── DiffViewer.tsx
    │   │   ├── EnvLabel.tsx
    │   │   ├── ItemBadge.tsx
    │   │   ├── LangfuseLogo.tsx
    │   │   ├── LocalIsoDate.tsx
    │   │   ├── ModelParameters
    │   │   │   ├── LLMApiKeyComponent.tsx
    │   │   │   └── index.tsx
    │   │   ├── NoDataOrLoading.tsx
    │   │   ├── PagedSettingsContainer.tsx
    │   │   ├── PosthogLogo.tsx
    │   │   ├── SettingsDangerZone.tsx
    │   │   ├── Slider.tsx
    │   │   ├── VersionLabel.tsx
    │   │   ├── date-picker.tsx
    │   │   ├── date-range-dropdowns.tsx
    │   │   ├── deleteButton.tsx
    │   │   ├── editor
    │   │   │   ├── CodeMirrorEditor.tsx
    │   │   │   ├── PromptLinkingEditor.tsx
    │   │   │   ├── dark-theme.ts
    │   │   │   ├── index.ts
    │   │   │   ├── light-theme.ts
    │   │   │   └── shared-theme.ts
    │   │   ├── error-page.tsx
    │   │   ├── grouped-score-badge.tsx
    │   │   ├── images
    │   │   │   ├── product_hunt_badge_dark.svg
    │   │   │   └── product_hunt_badge_light.svg
    │   │   ├── layouts
    │   │   │   ├── README.md
    │   │   │   ├── breadcrumb.tsx
    │   │   │   ├── container-page.tsx
    │   │   │   ├── doc-popup.tsx
    │   │   │   ├── header.tsx
    │   │   │   ├── layout.tsx
    │   │   │   ├── page-header.tsx
    │   │   │   ├── page.tsx
    │   │   │   ├── routes.tsx
    │   │   │   ├── settings-table-card.tsx
    │   │   │   ├── spinner.tsx
    │   │   │   └── status-badge.tsx
    │   │   ├── level-colors.tsx
    │   │   ├── level-counts-display.tsx
    │   │   ├── nav
    │   │   │   ├── app-sidebar.tsx
    │   │   │   ├── nav-main.tsx
    │   │   │   ├── nav-user.tsx
    │   │   │   ├── sidebar-notifications.tsx
    │   │   │   └── support-menu-dropdown.tsx
    │   │   ├── onboarding
    │   │   │   ├── AnnotationQueuesOnboarding.tsx
    │   │   │   ├── DatasetsOnboarding.tsx
    │   │   │   ├── EvaluatorsOnboarding.tsx
    │   │   │   ├── PromptsOnboarding.tsx
    │   │   │   ├── ScoresOnboarding.tsx
    │   │   │   ├── SessionsOnboarding.tsx
    │   │   │   ├── TracesOnboarding.tsx
    │   │   │   └── UsersOnboarding.tsx
    │   │   ├── projectNavigation.tsx
    │   │   ├── publish-object-switch.tsx
    │   │   ├── schemas
    │   │   │   ├── ChatMlSchema.ts
    │   │   │   └── MarkdownSchema.ts
    │   │   ├── scores-table-cell.tsx
    │   │   ├── session
    │   │   │   └── index.tsx
    │   │   ├── star-toggle.tsx
    │   │   ├── stats-cards.tsx
    │   │   ├── table
    │   │   │   ├── data-table-column-visibility-filter.tsx
    │   │   │   ├── data-table-multi-select-actions
    │   │   │   │   └── data-table-select-all-banner.tsx
    │   │   │   ├── data-table-pagination.tsx
    │   │   │   ├── data-table-row-height-switch.tsx
    │   │   │   ├── data-table-toolbar.tsx
    │   │   │   ├── data-table.tsx
    │   │   │   ├── peek.tsx
    │   │   │   ├── peek
    │   │   │   │   ├── hooks
    │   │   │   │   │   ├── useDatasetComparePeekNavigation.ts
    │   │   │   │   │   ├── useDatasetComparePeekState.ts
    │   │   │   │   │   ├── useEvalTemplatesPeekNavigation.ts
    │   │   │   │   │   ├── useObservationPeekNavigation.ts
    │   │   │   │   │   ├── useObservationPeekState.ts
    │   │   │   │   │   ├── usePeekData.ts
    │   │   │   │   │   ├── usePeekEvalConfigData.ts
    │   │   │   │   │   ├── usePeekEvalTemplateData.ts
    │   │   │   │   │   ├── usePeekState.ts
    │   │   │   │   │   ├── usePeekView.ts
    │   │   │   │   │   ├── useRunningEvaluatorsPeekNavigation.ts
    │   │   │   │   │   ├── useTracePeekNavigation.ts
    │   │   │   │   │   └── useTracePeekState.ts
    │   │   │   │   ├── peek-dataset-compare-detail.tsx
    │   │   │   │   ├── peek-evaluator-config-detail.tsx
    │   │   │   │   ├── peek-evaluator-template-detail.tsx
    │   │   │   │   ├── peek-observation-detail.tsx
    │   │   │   │   └── peek-trace-detail.tsx
    │   │   │   ├── table-id.tsx
    │   │   │   ├── table-link.tsx
    │   │   │   ├── table-view-presets
    │   │   │   │   ├── README.md
    │   │   │   │   ├── components
    │   │   │   │   │   └── data-table-view-presets-drawer.tsx
    │   │   │   │   ├── hooks
    │   │   │   │   │   ├── useTableViewManager.ts
    │   │   │   │   │   ├── useViewData.ts
    │   │   │   │   │   └── useViewMutations.ts
    │   │   │   │   └── validation.ts
    │   │   │   ├── types.ts
    │   │   │   ├── use-cases
    │   │   │   │   ├── models.tsx
    │   │   │   │   ├── observations.tsx
    │   │   │   │   ├── score-configs.tsx
    │   │   │   │   ├── scores.tsx
    │   │   │   │   ├── sessions.tsx
    │   │   │   │   ├── traces.tsx
    │   │   │   │   └── useFullTextSearch.tsx
    │   │   │   └── utils
    │   │   │   │   └── joinTableCoreAndMetrics.ts
    │   │   ├── token-usage-badge.tsx
    │   │   ├── trace
    │   │   │   ├── BreakdownToolTip.tsx
    │   │   │   ├── CopyIdsPopover.tsx
    │   │   │   ├── IOPreview.tsx
    │   │   │   ├── ObservationPreview.tsx
    │   │   │   ├── ObservationTree.tsx
    │   │   │   ├── TracePage.tsx
    │   │   │   ├── TracePreview.tsx
    │   │   │   ├── TraceTimelineView.tsx
    │   │   │   ├── index.tsx
    │   │   │   └── lib
    │   │   │   │   └── helpers.ts
    │   │   ├── ui
    │   │   │   ├── CodeJsonViewer.tsx
    │   │   │   ├── Codeblock.tsx
    │   │   │   ├── LangfuseMediaView.tsx
    │   │   │   ├── MarkdownJsonView.tsx
    │   │   │   ├── MarkdownViewer.tsx
    │   │   │   ├── accordion.tsx
    │   │   │   ├── alert.tsx
    │   │   │   ├── avatar.tsx
    │   │   │   ├── badge.tsx
    │   │   │   ├── breadcrumb.tsx
    │   │   │   ├── button.tsx
    │   │   │   ├── calendar.tsx
    │   │   │   ├── card.tsx
    │   │   │   ├── chart.tsx
    │   │   │   ├── checkbox.tsx
    │   │   │   ├── collapsible.tsx
    │   │   │   ├── command.tsx
    │   │   │   ├── dialog.tsx
    │   │   │   ├── drawer.tsx
    │   │   │   ├── dropdown-menu.tsx
    │   │   │   ├── form.tsx
    │   │   │   ├── hover-card.tsx
    │   │   │   ├── input-command.tsx
    │   │   │   ├── input.tsx
    │   │   │   ├── label.tsx
    │   │   │   ├── password-input.tsx
    │   │   │   ├── popover.tsx
    │   │   │   ├── progress.tsx
    │   │   │   ├── radio-group.tsx
    │   │   │   ├── resizable-image.tsx
    │   │   │   ├── resizable.tsx
    │   │   │   ├── scroll-area.tsx
    │   │   │   ├── select.tsx
    │   │   │   ├── separator.tsx
    │   │   │   ├── sheet.tsx
    │   │   │   ├── side-panel.tsx
    │   │   │   ├── sidebar.tsx
    │   │   │   ├── skeleton.tsx
    │   │   │   ├── slider.tsx
    │   │   │   ├── sonner.tsx
    │   │   │   ├── splash-screen.tsx
    │   │   │   ├── switch.tsx
    │   │   │   ├── table.tsx
    │   │   │   ├── tabs-bar.tsx
    │   │   │   ├── tabs.tsx
    │   │   │   ├── textarea.tsx
    │   │   │   ├── time-icon.tsx
    │   │   │   ├── time-period-select.tsx
    │   │   │   ├── time-picker-input.tsx
    │   │   │   ├── time-picker-utils.tsx
    │   │   │   ├── time-picker.tsx
    │   │   │   ├── timeline.tsx
    │   │   │   ├── toggle-group.tsx
    │   │   │   ├── toggle.tsx
    │   │   │   └── tooltip.tsx
    │   │   ├── useLocalStorage.tsx
    │   │   └── useSessionStorage.tsx
    │   ├── constants
    │   │   ├── VERSION.ts
    │   │   └── index.ts
    │   ├── ee
    │   │   ├── README.md
    │   │   └── features
    │   │   │   ├── audit-log-viewer
    │   │   │       ├── AuditLogsSettingsPage.tsx
    │   │   │       └── AuditLogsTable.tsx
    │   │   │   ├── billing
    │   │   │       ├── README.md
    │   │   │       ├── components
    │   │   │       │   ├── BillingSettings.tsx
    │   │   │       │   ├── SupportOrUpgradePage.tsx
    │   │   │       │   └── UsageTracker.tsx
    │   │   │       ├── constants.ts
    │   │   │       ├── server
    │   │   │       │   ├── cloudBillingRouter.ts
    │   │   │       │   └── stripeWebhookApiHandler.ts
    │   │   │       ├── stripeClientReference.ts
    │   │   │       └── utils
    │   │   │       │   ├── stripe.ts
    │   │   │       │   └── stripeProducts.ts
    │   │   │   ├── multi-tenant-sso
    │   │   │       ├── createNewSsoConfigHandler.ts
    │   │   │       ├── multiTenantSsoAvailable.ts
    │   │   │       ├── types.ts
    │   │   │       └── utils.ts
    │   │   │   ├── sso-settings
    │   │   │       └── components
    │   │   │       │   └── SSOSettings.tsx
    │   │   │   └── ui-customization
    │   │   │       ├── productModuleSchema.ts
    │   │   │       ├── uiCustomizationRouter.ts
    │   │   │       └── useUiCustomization.ts
    │   ├── env.mjs
    │   ├── features
    │   │   ├── README.md
    │   │   ├── admin-api
    │   │   │   ├── memberships.ts
    │   │   │   ├── organizations
    │   │   │   │   ├── apiKeys
    │   │   │   │   │   ├── apiKeyById.ts
    │   │   │   │   │   └── index.ts
    │   │   │   │   ├── index.ts
    │   │   │   │   └── organizationById.ts
    │   │   │   ├── projects.ts
    │   │   │   ├── projects
    │   │   │   │   ├── createProject.ts
    │   │   │   │   └── projectById
    │   │   │   │   │   ├── apiKeys
    │   │   │   │   │       ├── apiKeyById.ts
    │   │   │   │   │       └── index.ts
    │   │   │   │   │   ├── index.ts
    │   │   │   │   │   └── memberships
    │   │   │   │   │       └── index.ts
    │   │   │   └── server
    │   │   │   │   └── adminApiAuth.ts
    │   │   ├── annotation-queues
    │   │   │   ├── components
    │   │   │   │   ├── AnnotationQueueItemPage.tsx
    │   │   │   │   ├── AnnotationQueueItemsTable.tsx
    │   │   │   │   ├── AnnotationQueuesItem.tsx
    │   │   │   │   ├── AnnotationQueuesTable.tsx
    │   │   │   │   ├── CreateNewAnnotationQueueItem.tsx
    │   │   │   │   ├── CreateOrEditAnnotationQueueButton.tsx
    │   │   │   │   └── DeleteAnnotationQueueButton.tsx
    │   │   │   ├── pages
    │   │   │   │   ├── AnnotationQueueItems.tsx
    │   │   │   │   └── AnnotationQueues.tsx
    │   │   │   └── server
    │   │   │   │   ├── annotationQueueItems.ts
    │   │   │   │   └── annotationQueues.ts
    │   │   ├── audit-logs
    │   │   │   └── auditLog.ts
    │   │   ├── auth-credentials
    │   │   │   ├── components
    │   │   │   │   ├── ResetPasswordButton.tsx
    │   │   │   │   └── ResetPasswordPage.tsx
    │   │   │   ├── lib
    │   │   │   │   ├── credentialsServerUtils.ts
    │   │   │   │   └── credentialsUtils.ts
    │   │   │   └── server
    │   │   │   │   ├── credentialsRouter.ts
    │   │   │   │   └── signupApiHandler.ts
    │   │   ├── auth
    │   │   │   ├── components
    │   │   │   │   ├── AuthCloudPrivacyNotice.tsx
    │   │   │   │   └── AuthCloudRegionSwitch.tsx
    │   │   │   ├── hooks.ts
    │   │   │   └── lib
    │   │   │   │   ├── createProjectMembershipsOnSignup.ts
    │   │   │   │   ├── projectNameSchema.ts
    │   │   │   │   ├── projectRetentionSchema.ts
    │   │   │   │   └── signupSchema.ts
    │   │   ├── background-migrations
    │   │   │   ├── components
    │   │   │   │   ├── background-migrations.tsx
    │   │   │   │   └── retry-background-migration.tsx
    │   │   │   └── server
    │   │   │   │   └── background-migrations-router.ts
    │   │   ├── batch-exports
    │   │   │   ├── README.md
    │   │   │   ├── components
    │   │   │   │   ├── BatchExportsSettingsPage.tsx
    │   │   │   │   └── BatchExportsTable.tsx
    │   │   │   └── server
    │   │   │   │   └── batchExport.ts
    │   │   ├── blobstorage-integration
    │   │   │   ├── blobstorage-integration-router.ts
    │   │   │   └── types.ts
    │   │   ├── cloud-status-notification
    │   │   │   ├── components
    │   │   │   │   └── CloudStatusMenu.tsx
    │   │   │   ├── server
    │   │   │   │   └── cloud-status-router.ts
    │   │   │   └── types.ts
    │   │   ├── column-visibility
    │   │   │   └── hooks
    │   │   │   │   ├── useColumnOrder.ts
    │   │   │   │   └── useColumnVisibility.ts
    │   │   ├── command-k-menu
    │   │   │   ├── CommandMenu.tsx
    │   │   │   └── CommandMenuProvider.tsx
    │   │   ├── comments
    │   │   │   ├── CommentCountIcon.tsx
    │   │   │   ├── CommentDrawerButton.tsx
    │   │   │   ├── CommentList.tsx
    │   │   │   └── validateCommentReferenceObject.ts
    │   │   ├── dashboard
    │   │   │   ├── components
    │   │   │   │   ├── BaseTimeSeriesChart.tsx
    │   │   │   │   ├── ChartScores.tsx
    │   │   │   │   ├── DashboardTable.tsx
    │   │   │   │   ├── EditDashboardDialog.tsx
    │   │   │   │   ├── LatencyChart.tsx
    │   │   │   │   ├── LatencyTables.tsx
    │   │   │   │   ├── LeftAlignedCell.tsx
    │   │   │   │   ├── ModelCostTable.tsx
    │   │   │   │   ├── ModelSelector.tsx
    │   │   │   │   ├── ModelUsageChart.tsx
    │   │   │   │   ├── RightAlignedCell.tsx
    │   │   │   │   ├── ScoresTable.tsx
    │   │   │   │   ├── SelectDashboardDialog.tsx
    │   │   │   │   ├── TabTimeSeriesChart.tsx
    │   │   │   │   ├── TabsComponent.tsx
    │   │   │   │   ├── Tooltip.tsx
    │   │   │   │   ├── TotalMetric.tsx
    │   │   │   │   ├── TracesBarListChart.tsx
    │   │   │   │   ├── TracesTimeSeriesChart.tsx
    │   │   │   │   ├── UserChart.tsx
    │   │   │   │   ├── cards
    │   │   │   │   │   ├── ChevronButton.tsx
    │   │   │   │   │   ├── DashboardCard.tsx
    │   │   │   │   │   └── DashboardTable.tsx
    │   │   │   │   ├── hooks.ts
    │   │   │   │   └── score-analytics
    │   │   │   │   │   ├── CategoricalScoreChart.tsx
    │   │   │   │   │   ├── NumericScoreHistogram.tsx
    │   │   │   │   │   ├── NumericScoreTimeSeriesChart.tsx
    │   │   │   │   │   └── ScoreAnalytics.tsx
    │   │   │   ├── lib
    │   │   │   │   ├── dashboard-utils.ts
    │   │   │   │   └── score-analytics-utils.ts
    │   │   │   ├── server
    │   │   │   │   └── dashboard-router.ts
    │   │   │   └── utils
    │   │   │   │   └── getColorsForCategories.tsx
    │   │   ├── datasets
    │   │   │   ├── components
    │   │   │   │   ├── DatasetActionButton.tsx
    │   │   │   │   ├── DatasetAggregateTableCell.tsx
    │   │   │   │   ├── DatasetAnalytics.tsx
    │   │   │   │   ├── DatasetCompareRunsTable.tsx
    │   │   │   │   ├── DatasetForm.tsx
    │   │   │   │   ├── DatasetItemsTable.tsx
    │   │   │   │   ├── DatasetRunAggregateColumnHelpers.tsx
    │   │   │   │   ├── DatasetRunItemsTable.tsx
    │   │   │   │   ├── DatasetRunsTable.tsx
    │   │   │   │   ├── DatasetsTable.tsx
    │   │   │   │   ├── DeleteDatasetRunButton.tsx
    │   │   │   │   ├── DuplicateDatasetButton.tsx
    │   │   │   │   ├── EditDatasetItem.tsx
    │   │   │   │   ├── ImportCard.tsx
    │   │   │   │   ├── NewDatasetItemButton.tsx
    │   │   │   │   ├── NewDatasetItemForm.tsx
    │   │   │   │   ├── NewDatasetItemFromExistingObject.tsx
    │   │   │   │   ├── PreviewCsvImport.tsx
    │   │   │   │   ├── UploadDatasetCsv.tsx
    │   │   │   │   └── UploadDatasetCsvButton.tsx
    │   │   │   ├── hooks
    │   │   │   │   └── useDatasetRunAggregateColumns.ts
    │   │   │   ├── lib
    │   │   │   │   ├── csvHelpers.ts
    │   │   │   │   └── findDefaultColumn.ts
    │   │   │   └── server
    │   │   │   │   ├── dataset-router.ts
    │   │   │   │   └── service.ts
    │   │   ├── entitlements
    │   │   │   ├── README.md
    │   │   │   ├── constants
    │   │   │   │   └── entitlements.ts
    │   │   │   ├── hooks.ts
    │   │   │   └── server
    │   │   │   │   ├── getPlan.ts
    │   │   │   │   ├── hasEntitlement.ts
    │   │   │   │   └── hasEntitlementLimit.ts
    │   │   ├── evals
    │   │   │   ├── components
    │   │   │   │   ├── deactivate-config.tsx
    │   │   │   │   ├── eval-form-descriptions.tsx
    │   │   │   │   ├── eval-log.tsx
    │   │   │   │   ├── eval-template-detail.tsx
    │   │   │   │   ├── eval-templates-table.tsx
    │   │   │   │   ├── evaluation-prompt-preview.tsx
    │   │   │   │   ├── evaluator-detail.tsx
    │   │   │   │   ├── evaluator-form.tsx
    │   │   │   │   ├── evaluator-selector.tsx
    │   │   │   │   ├── evaluator-table.tsx
    │   │   │   │   ├── execution-count-tooltip.tsx
    │   │   │   │   ├── inner-evaluator-form.tsx
    │   │   │   │   ├── maintainer-tooltip.tsx
    │   │   │   │   ├── manage-default-eval-model.tsx
    │   │   │   │   ├── ragas-logo.tsx
    │   │   │   │   ├── run-evaluator-form.tsx
    │   │   │   │   ├── select-evaluator-list.tsx
    │   │   │   │   ├── set-up-default-eval-model-card.tsx
    │   │   │   │   ├── template-form.tsx
    │   │   │   │   └── template-selector.tsx
    │   │   │   ├── hooks
    │   │   │   │   ├── useEvalConfigMappingData.ts
    │   │   │   │   ├── useEvalTargetCount.ts
    │   │   │   │   ├── useEvaluationModel.ts
    │   │   │   │   ├── useExtractVariables.ts
    │   │   │   │   ├── useSingleTemplateValidation.ts
    │   │   │   │   ├── useTemplateValidation.ts
    │   │   │   │   ├── useTemplatesValidation.ts
    │   │   │   │   └── useValidateCustomModel.ts
    │   │   │   ├── pages
    │   │   │   │   ├── default-evaluation-model.tsx
    │   │   │   │   ├── evaluators.tsx
    │   │   │   │   ├── new-evaluator.tsx
    │   │   │   │   ├── new-template.tsx
    │   │   │   │   └── templates.tsx
    │   │   │   ├── server
    │   │   │   │   ├── addDatasetRunItemsToEvalQueue.ts
    │   │   │   │   ├── defaultEvalModelRouter.ts
    │   │   │   │   └── router.ts
    │   │   │   ├── types.ts
    │   │   │   └── utils
    │   │   │   │   ├── evaluator-form-utils.ts
    │   │   │   │   ├── job-execution-utils.ts
    │   │   │   │   └── typeHelpers.ts
    │   │   ├── experiments
    │   │   │   ├── components
    │   │   │   │   └── CreateExperimentsForm.tsx
    │   │   │   ├── hooks
    │   │   │   │   ├── useEvaluatorDefaults.ts
    │   │   │   │   ├── useExperimentEvaluatorData.ts
    │   │   │   │   ├── useExperimentEvaluatorSelection.ts
    │   │   │   │   ├── useExperimentNameValidation.ts
    │   │   │   │   └── useExperimentPromptData.ts
    │   │   │   ├── server
    │   │   │   │   └── router.ts
    │   │   │   └── utils
    │   │   │   │   └── evaluatorMappingUtils.ts
    │   │   ├── feature-flags
    │   │   │   ├── README.md
    │   │   │   ├── available-flags.ts
    │   │   │   ├── components
    │   │   │   │   └── FeatureFlagToggle.tsx
    │   │   │   ├── hooks
    │   │   │   │   └── useIsFeatureEnabled.ts
    │   │   │   ├── types.ts
    │   │   │   └── utils.ts
    │   │   ├── feedback
    │   │   │   ├── component
    │   │   │   │   └── FeedbackButton.tsx
    │   │   │   └── server
    │   │   │   │   ├── corsMiddleware.ts
    │   │   │   │   └── feedbackHandler.ts
    │   │   ├── filters
    │   │   │   ├── components
    │   │   │   │   ├── filter-builder.tsx
    │   │   │   │   └── multi-select.tsx
    │   │   │   └── hooks
    │   │   │   │   └── useFilterState.ts
    │   │   ├── llm-api-key
    │   │   │   ├── server
    │   │   │   │   └── router.ts
    │   │   │   └── types.ts
    │   │   ├── llm-schemas
    │   │   │   ├── server
    │   │   │   │   └── router.ts
    │   │   │   └── validation.ts
    │   │   ├── llm-tools
    │   │   │   ├── server
    │   │   │   │   └── router.ts
    │   │   │   └── validation.ts
    │   │   ├── media
    │   │   │   ├── server
    │   │   │   │   ├── getFileExtensionFromContentType.ts
    │   │   │   │   └── getMediaStorageClient.ts
    │   │   │   └── validation.ts
    │   │   ├── models
    │   │   │   ├── components
    │   │   │   │   ├── CloneModelButton.tsx
    │   │   │   │   ├── DeleteModelButton.tsx
    │   │   │   │   ├── EditModelButton.tsx
    │   │   │   │   ├── ModelSettings.tsx
    │   │   │   │   ├── PriceBreakdownTooltip.tsx
    │   │   │   │   ├── PricePreview.tsx
    │   │   │   │   ├── PriceUnitSelector.tsx
    │   │   │   │   └── UpsertModelFormDrawer.tsx
    │   │   │   ├── hooks
    │   │   │   │   └── usePriceUnitMultiplier.ts
    │   │   │   ├── server
    │   │   │   │   └── isValidPostgresRegex.ts
    │   │   │   ├── utils.ts
    │   │   │   └── validation.ts
    │   │   ├── navigate-detail-pages
    │   │   │   ├── DetailPageNav.tsx
    │   │   │   └── context.tsx
    │   │   ├── notifications
    │   │   │   ├── ErrorNotification.tsx
    │   │   │   ├── Notification.tsx
    │   │   │   ├── SuccessNotification.tsx
    │   │   │   ├── showErrorToast.tsx
    │   │   │   ├── showSuccessToast.tsx
    │   │   │   └── showVersionUpdateToast.tsx
    │   │   ├── orderBy
    │   │   │   └── hooks
    │   │   │   │   ├── useOrderByState.clienttest.tsx
    │   │   │   │   └── useOrderByState.ts
    │   │   ├── organizations
    │   │   │   ├── components
    │   │   │   │   ├── DeleteOrganizationButton.tsx
    │   │   │   │   ├── NewOrganizationForm.tsx
    │   │   │   │   ├── ProjectOverview.tsx
    │   │   │   │   └── RenameOrganization.tsx
    │   │   │   ├── hooks.ts
    │   │   │   ├── server
    │   │   │   │   └── organizationRouter.ts
    │   │   │   └── utils
    │   │   │   │   └── organizationNameSchema.ts
    │   │   ├── otel
    │   │   │   └── server
    │   │   │   │   ├── OtelIngestionProcessor.ts
    │   │   │   │   └── attributes.ts
    │   │   ├── playground
    │   │   │   ├── page
    │   │   │   │   ├── components
    │   │   │   │   │   ├── CreateOrEditLLMSchemaDialog.tsx
    │   │   │   │   │   ├── CreateOrEditLLMToolDialog.tsx
    │   │   │   │   │   ├── GenerationOutput.tsx
    │   │   │   │   │   ├── JumpToPlaygroundButton.tsx
    │   │   │   │   │   ├── Messages.tsx
    │   │   │   │   │   ├── PlaygroundTools
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   ├── PromptVariableComponent.tsx
    │   │   │   │   │   ├── ResetPlaygroundButton.tsx
    │   │   │   │   │   ├── SaveToPromptButton.tsx
    │   │   │   │   │   ├── StructuredOutputSchemaSection.tsx
    │   │   │   │   │   └── Variables.tsx
    │   │   │   │   ├── context
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── hooks
    │   │   │   │   │   ├── useCommandEnter.ts
    │   │   │   │   │   ├── useModelParams.ts
    │   │   │   │   │   └── usePlaygroundCache.ts
    │   │   │   │   ├── index.tsx
    │   │   │   │   ├── playground.tsx
    │   │   │   │   └── types.ts
    │   │   │   └── server
    │   │   │   │   ├── analytics
    │   │   │   │       └── posthogCallback.ts
    │   │   │   │   ├── authorizeRequest.ts
    │   │   │   │   ├── chatCompletionHandler.ts
    │   │   │   │   └── validateChatCompletionBody.ts
    │   │   ├── posthog-analytics
    │   │   │   ├── ServerPosthog.ts
    │   │   │   └── usePostHogClientCapture.ts
    │   │   ├── posthog-integration
    │   │   │   ├── posthog-integration-router.ts
    │   │   │   └── types.ts
    │   │   ├── projects
    │   │   │   ├── components
    │   │   │   │   ├── ConfigureRetention.tsx
    │   │   │   │   ├── DeleteProjectButton.tsx
    │   │   │   │   ├── HostNameProject.tsx
    │   │   │   │   ├── NewProjectForm.tsx
    │   │   │   │   ├── RenameProject.tsx
    │   │   │   │   └── TransferProjectButton.tsx
    │   │   │   ├── hooks.ts
    │   │   │   └── server
    │   │   │   │   └── projectsRouter.ts
    │   │   ├── prompts
    │   │   │   ├── README.md
    │   │   │   ├── components
    │   │   │   │   ├── NewPromptForm
    │   │   │   │   │   ├── PromptChatMessages.tsx
    │   │   │   │   │   ├── ReviewPromptDialog.tsx
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   └── validation.ts
    │   │   │   │   ├── PromptSelectionDialog.tsx
    │   │   │   │   ├── PromptVariableListPreview.tsx
    │   │   │   │   ├── PromptVersionDiffDialog.tsx
    │   │   │   │   ├── ProtectedLabelsSettings.tsx
    │   │   │   │   ├── SetPromptVersionLabels
    │   │   │   │   │   ├── AddLabelForm.tsx
    │   │   │   │   │   ├── LabelCommandItem.tsx
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── auto-complete.tsx
    │   │   │   │   ├── delete-prompt-version.tsx
    │   │   │   │   ├── delete-prompt.tsx
    │   │   │   │   ├── duplicate-prompt.tsx
    │   │   │   │   ├── prompt-detail.tsx
    │   │   │   │   ├── prompt-history.tsx
    │   │   │   │   ├── prompt-new.tsx
    │   │   │   │   ├── prompts-table.tsx
    │   │   │   │   └── renderContentWithPromptButtons.tsx
    │   │   │   ├── constants.ts
    │   │   │   ├── hooks
    │   │   │   │   └── usePromptNameValidation.tsx
    │   │   │   ├── server
    │   │   │   │   ├── actions
    │   │   │   │   │   ├── createPrompt.ts
    │   │   │   │   │   ├── getPromptByName.ts
    │   │   │   │   │   ├── getPromptsMeta.ts
    │   │   │   │   │   └── updatePrompts.ts
    │   │   │   │   ├── handlers
    │   │   │   │   │   ├── promptNameHandler.ts
    │   │   │   │   │   ├── promptVersionHandler.ts
    │   │   │   │   │   └── promptsHandler.ts
    │   │   │   │   ├── routers
    │   │   │   │   │   └── promptRouter.ts
    │   │   │   │   └── utils
    │   │   │   │   │   ├── authorizePromptRequest.ts
    │   │   │   │   │   ├── checkHasProtectedLabels.ts
    │   │   │   │   │   ├── updatePromptLabels.ts
    │   │   │   │   │   ├── updatePromptTags.ts
    │   │   │   │   │   └── validation.ts
    │   │   │   └── utils.ts
    │   │   ├── public-api
    │   │   │   ├── README.md
    │   │   │   ├── components
    │   │   │   │   ├── ApiKeyList.tsx
    │   │   │   │   ├── CreateApiKeyButton.tsx
    │   │   │   │   ├── CreateLLMApiKeyDialog.tsx
    │   │   │   │   ├── CreateLLMApiKeyForm.tsx
    │   │   │   │   ├── LLMApiKeyList.tsx
    │   │   │   │   ├── QuickstartExamples.tsx
    │   │   │   │   └── UpdateLLMApiKeyDialog.tsx
    │   │   │   ├── server
    │   │   │   │   ├── RateLimitService.ts
    │   │   │   │   ├── apiAuth.ts
    │   │   │   │   ├── cors.ts
    │   │   │   │   ├── createAuthedProjectAPIRoute.ts
    │   │   │   │   ├── dailyMetrics.ts
    │   │   │   │   ├── filter-builder.ts
    │   │   │   │   ├── observations.ts
    │   │   │   │   ├── organizationApiKeyRouter.ts
    │   │   │   │   ├── projectApiKeyRouter.ts
    │   │   │   │   ├── scores-api-service.ts
    │   │   │   │   ├── scores.ts
    │   │   │   │   ├── traces.ts
    │   │   │   │   └── withMiddlewares.ts
    │   │   │   └── types
    │   │   │   │   ├── annotation-queues.ts
    │   │   │   │   ├── comments.ts
    │   │   │   │   ├── datasets.ts
    │   │   │   │   ├── events.ts
    │   │   │   │   ├── generations.ts
    │   │   │   │   ├── metrics.ts
    │   │   │   │   ├── models.ts
    │   │   │   │   ├── observations.ts
    │   │   │   │   ├── sessions.ts
    │   │   │   │   ├── spans.ts
    │   │   │   │   └── traces.ts
    │   │   ├── query
    │   │   │   ├── dashboardUiTableToViewMapping.ts
    │   │   │   ├── dataModel.ts
    │   │   │   ├── index.ts
    │   │   │   ├── server
    │   │   │   │   └── queryBuilder.ts
    │   │   │   └── types.ts
    │   │   ├── rbac
    │   │   │   ├── components
    │   │   │   │   ├── CreateProjectMemberButton.tsx
    │   │   │   │   ├── MembersTable.tsx
    │   │   │   │   ├── MembershipInvitesPage.tsx
    │   │   │   │   └── RoleSelectItem.tsx
    │   │   │   ├── constants
    │   │   │   │   ├── orderedRoles.ts
    │   │   │   │   ├── organizationAccessRights.ts
    │   │   │   │   └── projectAccessRights.ts
    │   │   │   ├── server
    │   │   │   │   ├── allInvitesRoutes.ts
    │   │   │   │   ├── allMembersRoutes.ts
    │   │   │   │   └── membersRouter.ts
    │   │   │   └── utils
    │   │   │   │   ├── checkOrganizationAccess.ts
    │   │   │   │   └── checkProjectAccess.ts
    │   │   ├── scores
    │   │   │   ├── adapters
    │   │   │   │   └── index.ts
    │   │   │   ├── components
    │   │   │   │   ├── AnnotateDrawer.tsx
    │   │   │   │   ├── AnnotateDrawerContent.tsx
    │   │   │   │   ├── CreateScoreConfigButton.tsx
    │   │   │   │   ├── ScoreChart.tsx
    │   │   │   │   ├── ScoreConfigDetails.tsx
    │   │   │   │   ├── ScoreConfigSettings.tsx
    │   │   │   │   ├── ScoreDetailColumnHelpers.tsx
    │   │   │   │   ├── TimeseriesChart.tsx
    │   │   │   │   └── multi-select-key-values.tsx
    │   │   │   ├── hooks
    │   │   │   │   ├── useIndividualScoreColumns.ts
    │   │   │   │   ├── useScoreCustomOptimistic.ts
    │   │   │   │   ├── useScoreMutations.ts
    │   │   │   │   └── useScoreValues.ts
    │   │   │   ├── lib
    │   │   │   │   ├── aggregateScores.ts
    │   │   │   │   ├── getDefaultScoreData.ts
    │   │   │   │   ├── helpers.ts
    │   │   │   │   └── types.ts
    │   │   │   ├── schema.ts
    │   │   │   └── types.ts
    │   │   ├── setup
    │   │   │   ├── components
    │   │   │   │   ├── SetupPage.tsx
    │   │   │   │   └── SetupTracingButton.tsx
    │   │   │   └── setupRoutes.ts
    │   │   ├── slack
    │   │   │   └── server
    │   │   │   │   └── slack-webhook.ts
    │   │   ├── support-chat
    │   │   │   ├── PlainChat.tsx
    │   │   │   ├── createSupportEmailHash.ts
    │   │   │   └── trpc
    │   │   │   │   └── plain.ts
    │   │   ├── table
    │   │   │   ├── components
    │   │   │   │   ├── TableActionDialog.tsx
    │   │   │   │   ├── TableActionMenu.tsx
    │   │   │   │   ├── TableActionTargetOptions.tsx
    │   │   │   │   ├── TableSelectionManager.tsx
    │   │   │   │   └── targetOptionsQueryMap.tsx
    │   │   │   ├── hooks
    │   │   │   │   └── useSelectAll.ts
    │   │   │   ├── server
    │   │   │   │   ├── createBatchActionJob.ts
    │   │   │   │   ├── helpers.ts
    │   │   │   │   └── tableRouter.ts
    │   │   │   └── types.ts
    │   │   ├── tag
    │   │   │   ├── components
    │   │   │   │   ├── TagButton.tsx
    │   │   │   │   ├── TagCommandItem.tsx
    │   │   │   │   ├── TagCreateItem.tsx
    │   │   │   │   ├── TagInput.tsx
    │   │   │   │   ├── TagList.tsx
    │   │   │   │   ├── TagMananger.tsx
    │   │   │   │   ├── TagPromptDetailsPopover.tsx
    │   │   │   │   ├── TagPromptPopover.tsx
    │   │   │   │   ├── TagTraceDetailsPopover.tsx
    │   │   │   │   └── TagTracePopver.tsx
    │   │   │   └── hooks
    │   │   │   │   └── useTagManager.tsx
    │   │   ├── telemetry
    │   │   │   ├── README.md
    │   │   │   └── index.ts
    │   │   ├── theming
    │   │   │   ├── ThemeProvider.tsx
    │   │   │   ├── ThemeToggle.tsx
    │   │   │   └── useMarkdownContext.tsx
    │   │   ├── trace-graph-view
    │   │   │   ├── components
    │   │   │   │   ├── TraceGraphCanvas.tsx
    │   │   │   │   └── TraceGraphView.tsx
    │   │   │   └── types.ts
    │   │   └── widgets
    │   │   │   ├── chart-library
    │   │   │       ├── BigNumber.tsx
    │   │   │       ├── Chart.tsx
    │   │   │       ├── HistogramChart.tsx
    │   │   │       ├── HorizontalBarChart.tsx
    │   │   │       ├── LineChartTimeSeries.tsx
    │   │   │       ├── PieChart.tsx
    │   │   │       ├── VerticalBarChart.tsx
    │   │   │       ├── VerticalBarChartTimeSeries.tsx
    │   │   │       ├── chart-props.ts
    │   │   │       └── utils.ts
    │   │   │   ├── components
    │   │   │       ├── DashboardGrid.tsx
    │   │   │       ├── DashboardWidget.tsx
    │   │   │       ├── SelectWidgetDialog.tsx
    │   │   │       ├── WidgetForm.tsx
    │   │   │       ├── WidgetPropertySelectItem.tsx
    │   │   │       └── WidgetTable.tsx
    │   │   │   ├── index.ts
    │   │   │   └── utils.ts
    │   ├── hooks
    │   │   ├── use-element-visibility.tsx
    │   │   ├── use-environment-filter.tsx
    │   │   ├── use-mobile.tsx
    │   │   ├── useDashboardDateRange.tsx
    │   │   ├── useDebounce.tsx
    │   │   ├── useProjectIdFromURL.ts
    │   │   ├── useTableDateRange.tsx
    │   │   └── useUniqueNameValidation.tsx
    │   ├── initialize.ts
    │   ├── instrumentation.ts
    │   ├── observability.config.ts
    │   ├── pages
    │   │   ├── _app.tsx
    │   │   ├── api
    │   │   │   ├── admin
    │   │   │   │   ├── api-keys
    │   │   │   │   │   └── index.ts
    │   │   │   │   ├── bullmq
    │   │   │   │   │   └── index.ts
    │   │   │   │   └── organizations
    │   │   │   │   │   ├── [organizationId]
    │   │   │   │   │       ├── apiKeys
    │   │   │   │   │       │   ├── [apiKeyId].ts
    │   │   │   │   │       │   └── index.ts
    │   │   │   │   │       └── index.ts
    │   │   │   │   │   └── index.ts
    │   │   │   ├── auth
    │   │   │   │   ├── [...nextauth].ts
    │   │   │   │   ├── add-sso-config.ts
    │   │   │   │   ├── check-sso.ts
    │   │   │   │   └── signup.ts
    │   │   │   ├── billing
    │   │   │   │   └── README.md
    │   │   │   ├── feedback.ts
    │   │   │   ├── public
    │   │   │   │   ├── annotation-queues
    │   │   │   │   │   ├── [queueId].ts
    │   │   │   │   │   ├── [queueId]
    │   │   │   │   │   │   └── items
    │   │   │   │   │   │   │   ├── [itemId].ts
    │   │   │   │   │   │   │   └── index.ts
    │   │   │   │   │   └── index.ts
    │   │   │   │   ├── comments
    │   │   │   │   │   ├── [commentId].ts
    │   │   │   │   │   └── index.ts
    │   │   │   │   ├── dataset-items
    │   │   │   │   │   ├── [datasetItemId].ts
    │   │   │   │   │   └── index.ts
    │   │   │   │   ├── dataset-run-items.ts
    │   │   │   │   ├── datasets.ts
    │   │   │   │   ├── datasets
    │   │   │   │   │   └── [name]
    │   │   │   │   │   │   ├── index.ts
    │   │   │   │   │   │   └── runs
    │   │   │   │   │   │       ├── [runName].ts
    │   │   │   │   │   │       └── index.ts
    │   │   │   │   ├── events.ts
    │   │   │   │   ├── generations.ts
    │   │   │   │   ├── health.ts
    │   │   │   │   ├── ingestion.ts
    │   │   │   │   ├── media
    │   │   │   │   │   ├── [mediaId].ts
    │   │   │   │   │   └── index.ts
    │   │   │   │   ├── metrics
    │   │   │   │   │   ├── daily.ts
    │   │   │   │   │   └── index.ts
    │   │   │   │   ├── models
    │   │   │   │   │   ├── [modelId]
    │   │   │   │   │   │   └── index.ts
    │   │   │   │   │   └── index.ts
    │   │   │   │   ├── observations
    │   │   │   │   │   ├── [observationId].ts
    │   │   │   │   │   └── index.ts
    │   │   │   │   ├── organizations
    │   │   │   │   │   ├── memberships
    │   │   │   │   │   │   └── index.ts
    │   │   │   │   │   └── projects
    │   │   │   │   │   │   └── index.ts
    │   │   │   │   ├── otel
    │   │   │   │   │   ├── otlp-proto
    │   │   │   │   │   │   ├── README.md
    │   │   │   │   │   │   └── generated
    │   │   │   │   │   │   │   └── root.ts
    │   │   │   │   │   └── v1
    │   │   │   │   │   │   ├── metrics
    │   │   │   │   │   │       └── index.ts
    │   │   │   │   │   │   └── traces
    │   │   │   │   │   │       └── index.ts
    │   │   │   │   ├── projects
    │   │   │   │   │   ├── [projectId]
    │   │   │   │   │   │   ├── apiKeys
    │   │   │   │   │   │   │   ├── [apiKeyId].ts
    │   │   │   │   │   │   │   └── index.ts
    │   │   │   │   │   │   ├── index.ts
    │   │   │   │   │   │   └── memberships
    │   │   │   │   │   │   │   └── index.ts
    │   │   │   │   │   └── index.ts
    │   │   │   │   ├── prompts.ts
    │   │   │   │   ├── ready.ts
    │   │   │   │   ├── scim
    │   │   │   │   │   ├── ResourceTypes.ts
    │   │   │   │   │   ├── Schemas.ts
    │   │   │   │   │   ├── ServiceProviderConfig.ts
    │   │   │   │   │   └── Users
    │   │   │   │   │   │   ├── [id].ts
    │   │   │   │   │   │   └── index.ts
    │   │   │   │   ├── score-configs
    │   │   │   │   │   ├── [configId].ts
    │   │   │   │   │   └── index.ts
    │   │   │   │   ├── scores
    │   │   │   │   │   ├── [scoreId].ts
    │   │   │   │   │   └── index.ts
    │   │   │   │   ├── sessions
    │   │   │   │   │   ├── [sessionId].ts
    │   │   │   │   │   └── index.ts
    │   │   │   │   ├── spans.ts
    │   │   │   │   ├── traces
    │   │   │   │   │   ├── [traceId].ts
    │   │   │   │   │   └── index.ts
    │   │   │   │   └── v2
    │   │   │   │   │   ├── datasets
    │   │   │   │   │       ├── [datasetName]
    │   │   │   │   │       │   └── index.ts
    │   │   │   │   │       └── index.ts
    │   │   │   │   │   ├── prompts
    │   │   │   │   │       ├── [promptName]
    │   │   │   │   │       │   ├── index.ts
    │   │   │   │   │       │   └── versions
    │   │   │   │   │       │   │   └── [promptVersion].ts
    │   │   │   │   │       └── index.ts
    │   │   │   │   │   └── scores
    │   │   │   │   │       ├── [scoreId].ts
    │   │   │   │   │       └── index.ts
    │   │   │   └── trpc
    │   │   │   │   └── [trpc].ts
    │   │   ├── auth
    │   │   │   ├── error.tsx
    │   │   │   ├── hf-spaces.tsx
    │   │   │   ├── reset-password.tsx
    │   │   │   ├── sign-in.tsx
    │   │   │   └── sign-up.tsx
    │   │   ├── background-migrations.tsx
    │   │   ├── index.tsx
    │   │   ├── onboarding.tsx
    │   │   ├── organization
    │   │   │   └── [organizationId]
    │   │   │   │   ├── index.tsx
    │   │   │   │   ├── settings
    │   │   │   │       ├── [page].tsx
    │   │   │   │       └── index.tsx
    │   │   │   │   └── setup.tsx
    │   │   ├── project
    │   │   │   └── [projectId]
    │   │   │   │   ├── annotation-queues.tsx
    │   │   │   │   ├── annotation-queues
    │   │   │   │       └── [queueId]
    │   │   │   │       │   ├── index.tsx
    │   │   │   │       │   └── items
    │   │   │   │       │       ├── [itemId].tsx
    │   │   │   │       │       └── index.tsx
    │   │   │   │   ├── dashboards
    │   │   │   │       ├── [dashboardId]
    │   │   │   │       │   └── index.tsx
    │   │   │   │       ├── index.tsx
    │   │   │   │       └── new.tsx
    │   │   │   │   ├── datasets.tsx
    │   │   │   │   ├── datasets
    │   │   │   │       └── [datasetId]
    │   │   │   │       │   ├── compare.tsx
    │   │   │   │       │   ├── index.tsx
    │   │   │   │       │   ├── items.tsx
    │   │   │   │       │   ├── items
    │   │   │   │       │       └── [itemId].tsx
    │   │   │   │       │   └── runs
    │   │   │   │       │       └── [runId].tsx
    │   │   │   │   ├── evals
    │   │   │   │       ├── [evaluatorId].tsx
    │   │   │   │       ├── configs
    │   │   │   │       │   ├── [configId].tsx
    │   │   │   │       │   ├── index.tsx
    │   │   │   │       │   └── new.tsx
    │   │   │   │       ├── default-model.tsx
    │   │   │   │       ├── index.tsx
    │   │   │   │       ├── new.tsx
    │   │   │   │       └── templates
    │   │   │   │       │   ├── [id].tsx
    │   │   │   │       │   ├── index.tsx
    │   │   │   │       │   └── new.tsx
    │   │   │   │   ├── index.tsx
    │   │   │   │   ├── models.tsx
    │   │   │   │   ├── observations.tsx
    │   │   │   │   ├── playground.tsx
    │   │   │   │   ├── prompts
    │   │   │   │       ├── [promptName]
    │   │   │   │       │   ├── index.tsx
    │   │   │   │       │   └── metrics.tsx
    │   │   │   │       ├── index.tsx
    │   │   │   │       └── new.tsx
    │   │   │   │   ├── scores.tsx
    │   │   │   │   ├── sessions.tsx
    │   │   │   │   ├── sessions
    │   │   │   │       └── [sessionId].tsx
    │   │   │   │   ├── settings
    │   │   │   │       ├── [page].tsx
    │   │   │   │       ├── billing.ts
    │   │   │   │       ├── index.tsx
    │   │   │   │       ├── integrations
    │   │   │   │       │   ├── blobstorage.tsx
    │   │   │   │       │   └── posthog.tsx
    │   │   │   │       └── models
    │   │   │   │       │   └── [modelId].tsx
    │   │   │   │   ├── setup.tsx
    │   │   │   │   ├── traces.tsx
    │   │   │   │   ├── traces
    │   │   │   │       └── [traceId].tsx
    │   │   │   │   ├── users.tsx
    │   │   │   │   ├── users
    │   │   │   │       └── [userId].tsx
    │   │   │   │   └── widgets
    │   │   │   │       ├── [widgetId]
    │   │   │   │           └── index.tsx
    │   │   │   │       ├── index.tsx
    │   │   │   │       └── new.tsx
    │   │   ├── public
    │   │   │   └── traces
    │   │   │   │   └── [traceId].tsx
    │   │   ├── setup.tsx
    │   │   └── trace
    │   │   │   └── [traceId].tsx
    │   ├── server
    │   │   ├── api
    │   │   │   ├── definitions
    │   │   │   │   ├── evalConfigsTable.ts
    │   │   │   │   ├── evalExecutionsTable.ts
    │   │   │   │   ├── promptsTable.ts
    │   │   │   │   ├── scoresTable.ts
    │   │   │   │   └── usersTable.ts
    │   │   │   ├── root.ts
    │   │   │   ├── routers
    │   │   │   │   ├── auditLogs.ts
    │   │   │   │   ├── comments.ts
    │   │   │   │   ├── dashboardWidgets.ts
    │   │   │   │   ├── generations
    │   │   │   │   │   ├── db
    │   │   │   │   │   │   └── getAllGenerationsSqlQuery.ts
    │   │   │   │   │   ├── filterOptionsQuery.ts
    │   │   │   │   │   ├── getAllQueries.ts
    │   │   │   │   │   ├── index.ts
    │   │   │   │   │   └── utils
    │   │   │   │   │   │   └── GenerationTableOptions.ts
    │   │   │   │   ├── media.ts
    │   │   │   │   ├── models.ts
    │   │   │   │   ├── observations.ts
    │   │   │   │   ├── public.ts
    │   │   │   │   ├── scoreConfigs.ts
    │   │   │   │   ├── scores.ts
    │   │   │   │   ├── sessions.ts
    │   │   │   │   ├── tableViewPresets.ts
    │   │   │   │   ├── traces.ts
    │   │   │   │   ├── users.ts
    │   │   │   │   └── utilities.ts
    │   │   │   ├── services
    │   │   │   │   ├── sqlInterface.ts
    │   │   │   │   └── tableDefinitions.ts
    │   │   │   └── trpc.ts
    │   │   ├── auth.ts
    │   │   ├── db.ts
    │   │   └── utils
    │   │   │   ├── checkProjectMembershipOrAdmin.ts
    │   │   │   └── cookies.ts
    │   ├── styles
    │   │   └── globals.css
    │   └── utils
    │   │   ├── api.ts
    │   │   ├── clipboard.ts
    │   │   ├── date-range-utils.ts
    │   │   ├── dates.ts
    │   │   ├── exceptions.ts
    │   │   ├── getFinalModelParams.tsx
    │   │   ├── numbers.ts
    │   │   ├── shutdown.ts
    │   │   ├── string.ts
    │   │   ├── superjson.ts
    │   │   ├── tailwind.ts
    │   │   ├── tanstack.d.ts
    │   │   ├── trpcErrorToast.tsx
    │   │   └── types.ts
    ├── tailwind.config.ts
    ├── tsconfig.json
    └── types
    │   ├── global.d.ts
    │   └── next-auth.d.ts
└── worker
    ├── .eslintrc.js
    ├── Dockerfile
    ├── entrypoint.sh
    ├── package.json
    ├── src
        ├── __tests__
        │   ├── batchAction.test.ts
        │   ├── batchExport.test.ts
        │   ├── blobStorageIntegrationProcessing.test.ts
        │   ├── dataRetentionProcessing.test.ts
        │   ├── evalService.filtering.test.ts
        │   ├── evalService.test.ts
        │   ├── experimentsService.test.ts
        │   ├── modelMatch.test.ts
        │   ├── network.ts
        │   ├── projectDeletionProcessing.test.ts
        │   ├── redisConsumer.test.ts
        │   ├── scoreDeletion.test.ts
        │   ├── storageservice.test.ts
        │   ├── traceDeletion.test.ts
        │   └── utils.ts
        ├── api
        │   └── index.ts
        ├── app.ts
        ├── backgroundMigrations
        │   ├── IBackgroundMigration.ts
        │   ├── README.md
        │   ├── addGenerationsCostBackfill.ts
        │   ├── backgroundMigrationManager.ts
        │   ├── migrateEventLogToBlobStorageRefTable.ts
        │   ├── migrateObservationsFromPostgresToClickhouse.ts
        │   ├── migrateScoresFromPostgresToClickhouse.ts
        │   └── migrateTracesFromPostgresToClickhouse.ts
        ├── constants
        │   ├── VERSION.ts
        │   ├── default-model-prices.json
        │   ├── langfuse-dashboards.json
        │   └── managed-evaluators.json
        ├── database.ts
        ├── ee
        │   ├── cloudUsageMetering
        │   │   ├── constants.ts
        │   │   └── handleCloudUsageMeteringJob.ts
        │   ├── dataRetention
        │   │   ├── handleDataRetentionProcessingJob.ts
        │   │   └── handleDataRetentionSchedule.ts
        │   └── meteringDataPostgresExport
        │   │   └── handleMeteringDataPostgresExportJob.ts
        ├── env.ts
        ├── features
        │   ├── batchAction
        │   │   ├── handleBatchActionJob.ts
        │   │   └── processAddToQueue.ts
        │   ├── batchExport
        │   │   └── handleBatchExportJob.ts
        │   ├── blobstorage
        │   │   ├── handleBlobStorageIntegrationProjectJob.ts
        │   │   └── handleBlobStorageIntegrationSchedule.ts
        │   ├── database-read-stream
        │   │   ├── getDatabaseReadStream.ts
        │   │   └── types.ts
        │   ├── evaluation
        │   │   └── evalService.ts
        │   ├── experiments
        │   │   └── experimentService.ts
        │   ├── health
        │   │   └── index.ts
        │   ├── posthog
        │   │   ├── handlePostHogIntegrationProjectJob.ts
        │   │   └── handlePostHogIntegrationSchedule.ts
        │   ├── scores
        │   │   └── processClickhouseScoreDelete.ts
        │   ├── tokenisation
        │   │   ├── types.ts
        │   │   └── usage.ts
        │   ├── traces
        │   │   ├── processClickhouseTraceDelete.ts
        │   │   └── processPostgresTraceDelete.ts
        │   └── utilities.ts
        ├── index.ts
        ├── initialize.ts
        ├── instrumentation.ts
        ├── interfaces
        │   ├── ErrorResponse.ts
        │   └── MessageResponse.ts
        ├── middlewares.ts
        ├── queues
        │   ├── batchActionQueue.ts
        │   ├── batchExportQueue.ts
        │   ├── blobStorageIntegrationQueue.ts
        │   ├── cloudUsageMeteringQueue.ts
        │   ├── coreDataS3ExportQueue.ts
        │   ├── dataRetentionQueue.ts
        │   ├── evalQueue.ts
        │   ├── experimentQueue.ts
        │   ├── ingestionQueue.ts
        │   ├── postHogIntegrationQueue.ts
        │   ├── projectDelete.ts
        │   ├── scoreDelete.ts
        │   ├── traceDelete.ts
        │   └── workerManager.ts
        ├── scripts
        │   ├── createDefaultModelPricesJson.ts
        │   ├── refill-billing-event.ts
        │   ├── s3-ingestion-event-relpay.ts
        │   ├── upsertDefaultModelPrices.ts
        │   ├── upsertLangfuseDashboards.ts
        │   ├── upsertManagedEvaluators.ts
        │   └── verifyClickhouseRecords
        │   │   ├── README.md
        │   │   └── index.ts
        ├── services
        │   ├── ClickhouseWriter
        │   │   ├── ClickhouseWriter.unit.test.ts
        │   │   └── index.ts
        │   ├── IngestionService
        │   │   ├── index.ts
        │   │   ├── tests
        │   │   │   ├── IngestionService.integration.test.ts
        │   │   │   ├── IngestionService.unit.test.ts
        │   │   │   ├── calculateTokenCost.unit.test.ts
        │   │   │   └── utils.unit.test.ts
        │   │   └── utils.ts
        │   ├── dlq
        │   │   └── dlqRetryService.ts
        │   └── modelMatch.ts
        └── utils
        │   └── shutdown.ts
    └── tsconfig.json


/.codespellrc:
--------------------------------------------------------------------------------
1 | [codespell]
2 | skip = .git,*.pdf,*.svg,package-lock.json,*.prisma,pnpm-lock.yaml
3 | ignore-words-list = afterall,vertx,notIn
4 | 
5 | 


--------------------------------------------------------------------------------
/.cursor/environment.json:
--------------------------------------------------------------------------------
1 | {
2 |   "install": "cp .env.dev.example .env && pnpm i",
3 |   "build": {
4 |     "context": ".",
5 |     "dockerfile": "Dockerfile"
6 |   },
7 |   "start": "pnpm dx-f"
8 | }
9 | 


--------------------------------------------------------------------------------
/.cursor/rules/authorization-and-rbac.mdc:
--------------------------------------------------------------------------------
1 | ---
2 | description: How to manage authorization and RBAC within full-stack langfuse features
3 | globs: web/
4 | alwaysApply: true
5 | ---
6 | See [README.md](mdc:web/src/features/rbac/README.md) for details


--------------------------------------------------------------------------------
/.cursor/rules/entitlements.mdc:
--------------------------------------------------------------------------------
1 | ---
2 | description: How to enforce entitlements across full-stack features
3 | globs: web/**
4 | alwaysApply: true
5 | ---
6 | 
7 | Check [README.md](mdc:web/src/features/entitlements/README.md) to learn more about entitlements
8 | 


--------------------------------------------------------------------------------
/.cursor/rules/general-info.mdc:
--------------------------------------------------------------------------------
1 | ---
2 | description: 
3 | globs: 
4 | alwaysApply: true
5 | ---
6 | # General rules
7 | 
8 | - Linting in this repo only works if the development server is running


--------------------------------------------------------------------------------
/.dockerignore:
--------------------------------------------------------------------------------
1 | Dockerfile
2 | .dockerignore
3 | node_modules
4 | npm-debug.log
5 | README.md
6 | **/.next
7 | .git
8 | **/node_modules


--------------------------------------------------------------------------------
/.eslintignore:
--------------------------------------------------------------------------------
1 | node_modules
2 | **/node_modules
3 | build
4 | coverage


--------------------------------------------------------------------------------
/.github/CODEOWNERS:
--------------------------------------------------------------------------------
1 | # Currently inactive
2 | # * @langfuse/maintainers
3 | 


--------------------------------------------------------------------------------
/.github/DISCUSSION_TEMPLATE/ideas.yml:
--------------------------------------------------------------------------------
 1 | body:
 2 |   - type: textarea
 3 |     attributes:
 4 |       label: Describe the feature or potential improvement
 5 |       description: Please describe the change as clear and concise as possible. Remember to add context as to why you believe this is needed.
 6 |     validations:
 7 |       required: true
 8 |   - type: textarea
 9 |     attributes:
10 |       label: Additional information
11 |       description: Add any other information related to the change here. If your idea is related to any issues or discussions, link them here.
12 | 


--------------------------------------------------------------------------------
/.github/ISSUE_TEMPLATE/config.yml:
--------------------------------------------------------------------------------
1 | contact_links:
2 |   - name: 💡 Feature Request
3 |     url: https://github.com/orgs/langfuse/discussions/new?category=ideas
4 |     about: Suggest any ideas you have using our discussion forums.
5 |   - name: 🤗 Get Help
6 |     url: https://github.com/orgs/langfuse/discussions/new?category=support
7 |     about: If you can’t get something to work the way you expect, open a question in our discussion forums.
8 | 


--------------------------------------------------------------------------------
/.github/workflows/codespell.yml:
--------------------------------------------------------------------------------
 1 | ---
 2 | name: Codespell
 3 | 
 4 | on:
 5 |   push:
 6 |     branches:
 7 |       - "main"
 8 |     tags:
 9 |       - "v*"
10 |   pull_request:
11 |     branches:
12 |       - "**"
13 |   merge_group:
14 | 
15 | permissions:
16 |   contents: read
17 | 
18 | jobs:
19 |   codespell:
20 |     name: Check for spelling errors
21 |     runs-on: ubuntu-latest
22 | 
23 |     steps:
24 |       - name: Checkout
25 |         uses: actions/checkout@v3
26 |       - name: Codespell
27 |         uses: codespell-project/actions-codespell@v2
28 | 


--------------------------------------------------------------------------------
/.github/workflows/dependabot-rebase-stale.yml:
--------------------------------------------------------------------------------
 1 | name: Rebase Dependabot stale PRs
 2 | 
 3 | on:
 4 |   push:
 5 |     branches:
 6 |       - main
 7 |   workflow_dispatch:
 8 | 
 9 | jobs:
10 |   rebase-dependabot:
11 |     runs-on: ubuntu-latest
12 |     environment: "protected branches"
13 |     steps:
14 |       - name: "Rebase open Dependabot PR"
15 |         uses: orange-buffalo/dependabot-auto-rebase@v1
16 |         with:
17 |           api-token: ${{ secrets.GH_ACCESS_TOKEN }}
18 |           repository: ${{ github.repository }}
19 | 


--------------------------------------------------------------------------------
/.github/workflows/release.yml:
--------------------------------------------------------------------------------
 1 | on:
 2 |   workflow_dispatch:
 3 |   push:
 4 |     # Pattern matched against refs/tags
 5 |     tags:
 6 |       - "v3.[0-9]+.[0-9]+" # Semantic version tags
 7 | 
 8 | jobs:
 9 |   release:
10 |     runs-on: ubuntu-latest
11 |     environment: "protected branches"
12 |     steps:
13 |       - uses: actions/checkout@v4
14 |         with:
15 |           ref: main # Always checkout main even for tagged releases
16 |           fetch-depth: 0
17 |           token: ${{ secrets.GH_ACCESS_TOKEN }}
18 |       - name: Push to production
19 |         run: git push origin +main:production
20 | 


--------------------------------------------------------------------------------
/.npmrc:
--------------------------------------------------------------------------------
1 | public-hoist-pattern[]=*prisma*


--------------------------------------------------------------------------------
/.nvmrc:
--------------------------------------------------------------------------------
1 | v20


--------------------------------------------------------------------------------
/.vscode/extensions.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "recommendations": [
 3 |     "esbenp.prettier-vscode",
 4 |     "dbaeumer.vscode-eslint",
 5 |     "bradlc.vscode-tailwindcss",
 6 |     "unifiedjs.vscode-mdx",
 7 |     "yoavbls.pretty-ts-errors",
 8 |     "Prisma.prisma"
 9 |   ]
10 | }
11 | 


--------------------------------------------------------------------------------
/AGENTS.md:
--------------------------------------------------------------------------------
 1 | # Codex Guidelines for Langfuse
 2 | 
 3 | Langfuse is an **open source LLM engineering** platform for developing, monitoring, evaluating and debugging AI applications. See the README for more details.
 4 | 
 5 | ## Linting
 6 | - Run `pnpm run lint` to lint all packages.
 7 | - Fix issues automatically with `pnpm run lint:fix`.
 8 | 
 9 | ## Tests
10 | - Codex cannot run the test suite because it depends on Docker-based infrastructure that is unavailable in this environment.
11 | 
12 | ## Cursor Rules
13 | - Additional folder-specific rules live in `.cursor/rules/`.
14 | 
15 | ## Commits
16 | - Follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) when crafting commit messages.
17 | 


--------------------------------------------------------------------------------
/SECURITY.md:
--------------------------------------------------------------------------------
1 | ## Security Policy
2 | We strongly recommend using the latest version of Langfuse to receive all security updates.
3 | 
4 | For more information, please refer to the [Data Security & Privacy](https://langfuse.com/docs/data-security-privacy) page in the documentation or contact security@langfuse.com.
5 | 


--------------------------------------------------------------------------------
/ee/.eslintrc.js:
--------------------------------------------------------------------------------
1 | /** @type {import("eslint").Linter.Config} */
2 | module.exports = {
3 |   extends: ["@repo/eslint-config/library.js"],
4 |   parser: "@typescript-eslint/parser",
5 |   parserOptions: {
6 |     project: true,
7 |   },
8 | };
9 | 


--------------------------------------------------------------------------------
/ee/README.md:
--------------------------------------------------------------------------------
1 | # Enterprise Edition
2 | 
3 | This folder includes features that are only available in the Enterprise Edition of Langfuse and on Langfuse Cloud.
4 | 
5 | See [LICENSE](../LICENSE) and [docs](https://langfuse.com/docs/open-source) for more details.
6 | 


--------------------------------------------------------------------------------
/ee/src/ee-license-check/index.ts:
--------------------------------------------------------------------------------
1 | import { env } from "../env";
2 | 
3 | export const isEeAvailable: boolean =
4 |   env.NEXT_PUBLIC_LANGFUSE_CLOUD_REGION !== undefined ||
5 |   env.LANGFUSE_EE_LICENSE_KEY !== undefined;
6 | 


--------------------------------------------------------------------------------
/ee/src/env.ts:
--------------------------------------------------------------------------------
 1 | import { z } from "zod/v4";
 2 | import { removeEmptyEnvVariables } from "@langfuse/shared";
 3 | 
 4 | const EnvSchema = z.object({
 5 |   NEXT_PUBLIC_LANGFUSE_CLOUD_REGION: z.string().optional(),
 6 |   LANGFUSE_EE_LICENSE_KEY: z.string().optional(),
 7 | });
 8 | 
 9 | export const env = EnvSchema.parse(removeEmptyEnvVariables(process.env));
10 | 


--------------------------------------------------------------------------------
/ee/src/index.ts:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langfuse/langfuse/c8b282dc822c8cec556663f25a000eee58c0dbf6/ee/src/index.ts


--------------------------------------------------------------------------------
/ee/tsconfig.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "extends": "@repo/typescript-config/base.json",
 3 |   "compilerOptions": {
 4 |     "moduleResolution": "NodeNext",
 5 |     "module": "NodeNext",
 6 |     "lib": ["ES2020"],
 7 |     "outDir": "./dist",
 8 |     "types": ["node"],
 9 |     "target": "ES2020",
10 |     "rootDir": "."
11 |   },
12 |   "include": ["."],
13 |   "exclude": ["node_modules", "dist"]
14 | }
15 | 


--------------------------------------------------------------------------------
/fern/apis/client/definition/api.yml:
--------------------------------------------------------------------------------
 1 | name: langfuse
 2 | error-discrimination:
 3 |   strategy: status-code
 4 | auth: bearer
 5 | imports:
 6 |   commons: commons.yml
 7 | errors:
 8 |   - commons.Error
 9 |   - commons.UnauthorizedError
10 |   - commons.AccessDeniedError
11 |   - commons.MethodNotAllowedError
12 | 


--------------------------------------------------------------------------------
/fern/apis/client/definition/commons.yml:
--------------------------------------------------------------------------------
 1 | errors:
 2 |   Error:
 3 |     status-code: 400
 4 |     type: string
 5 |   UnauthorizedError:
 6 |     status-code: 401
 7 |     type: string
 8 |   AccessDeniedError:
 9 |     status-code: 403
10 |     type: string
11 |   MethodNotAllowedError:
12 |     status-code: 405
13 |     type: string
14 | 


--------------------------------------------------------------------------------
/fern/apis/organizations/definition/commons.yml:
--------------------------------------------------------------------------------
 1 | errors:
 2 |   Error:
 3 |     status-code: 400
 4 |     type: string
 5 |   UnauthorizedError:
 6 |     status-code: 401
 7 |     type: string
 8 |   AccessDeniedError:
 9 |     status-code: 403
10 |     type: string
11 |   MethodNotAllowedError:
12 |     status-code: 405
13 |     type: string
14 | 


--------------------------------------------------------------------------------
/fern/apis/organizations/generators.yml:
--------------------------------------------------------------------------------
 1 | default-group: local
 2 | groups:
 3 |   local:
 4 |     generators:
 5 |       - name: fernapi/fern-openapi
 6 |         version: 0.1.7
 7 |         output:
 8 |           location: local-file-system
 9 |           path: ../../../web/public/generated/organizations-api
10 |         config:
11 |           namespaceExport: Langfuse
12 |           allowCustomFetcher: true
13 |       - name: fernapi/fern-postman
14 |         version: 0.0.45
15 |         output:
16 |           location: local-file-system
17 |           path: ../../../web/public/generated/organizations-postman
18 | 


--------------------------------------------------------------------------------
/fern/fern.config.json:
--------------------------------------------------------------------------------
1 | {
2 |   "organization": "langfuse",
3 |   "version": "0.56.0"
4 | }
5 | 


--------------------------------------------------------------------------------
/generated/.gitignore:
--------------------------------------------------------------------------------
1 | python/


--------------------------------------------------------------------------------
/packages/config-eslint/package.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "name": "@repo/eslint-config",
 3 |   "version": "0.0.0",
 4 |   "license": "MIT",
 5 |   "private": true,
 6 |   "files": [
 7 |     "library.js",
 8 |     "next.js"
 9 |   ],
10 |   "devDependencies": {
11 |     "@typescript-eslint/eslint-plugin": "^7.1.0",
12 |     "@typescript-eslint/parser": "^7.12.0",
13 |     "@vercel/style-guide": "^6.0.0",
14 |     "eslint-config-next": "^14.2.15",
15 |     "eslint-config-prettier": "^9.1.0",
16 |     "eslint-config-turbo": "^1.13.4",
17 |     "eslint-plugin-only-warn": "^1.1.0",
18 |     "typescript": "^5.4.5"
19 |   }
20 | }
21 | 


--------------------------------------------------------------------------------
/packages/config-typescript/base.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "$schema": "https://json.schemastore.org/tsconfig",
 3 |   "display": "Default",
 4 |   "compilerOptions": {
 5 |     "composite": false,
 6 |     "declaration": true,
 7 |     "declarationMap": true,
 8 |     "esModuleInterop": true,
 9 |     "forceConsistentCasingInFileNames": true,
10 |     "inlineSources": false,
11 |     "isolatedModules": true,
12 |     "module": "ESNext",
13 |     "noErrorTruncation": true,
14 |     "moduleResolution": "Bundler",
15 |     "noUnusedLocals": false,
16 |     "noUnusedParameters": false,
17 |     "preserveWatchOutput": true,
18 |     "skipLibCheck": true,
19 |     "strict": true
20 |   },
21 |   "exclude": ["node_modules"]
22 | }
23 | 


--------------------------------------------------------------------------------
/packages/config-typescript/package.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "name": "@repo/typescript-config",
 3 |   "license": "MIT",
 4 |   "version": "0.0.0",
 5 |   "private": true,
 6 |   "publishConfig": {
 7 |     "access": "public"
 8 |   }
 9 | }
10 | 


--------------------------------------------------------------------------------
/packages/shared/.eslintrc.js:
--------------------------------------------------------------------------------
1 | /** @type {import("eslint").Linter.Config} */
2 | module.exports = {
3 |   extends: ["@repo/eslint-config/library.js"],
4 |   parser: "@typescript-eslint/parser",
5 |   parserOptions: {
6 |     project: true,
7 |   },
8 | };
9 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0001_traces.down.sql:
--------------------------------------------------------------------------------
1 | DROP TABLE traces ON CLUSTER default;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0002_observations.down.sql:
--------------------------------------------------------------------------------
1 | DROP TABLE observations ON CLUSTER default;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0003_scores.down.sql:
--------------------------------------------------------------------------------
1 | DROP TABLE scores ON CLUSTER default;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0004_drop_observations_index.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE observations ON CLUSTER default ADD INDEX IF NOT EXISTS idx_project_id project_id TYPE bloom_filter() GRANULARITY 1;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0004_drop_observations_index.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE observations ON CLUSTER default DROP INDEX IF EXISTS idx_project_id;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0005_add_session_id_index.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE traces ON CLUSTER default DROP INDEX IF EXISTS idx_session_id;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0005_add_session_id_index.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE traces ON CLUSTER default ADD INDEX IF NOT EXISTS idx_session_id session_id TYPE bloom_filter() GRANULARITY 1;
2 | ALTER TABLE traces ON CLUSTER default MATERIALIZE INDEX IF EXISTS idx_session_id;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0006_add_user_id_index.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE traces ON CLUSTER default DROP INDEX IF EXISTS idx_user_id;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0006_add_user_id_index.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE traces ON CLUSTER default ADD INDEX IF NOT EXISTS idx_user_id user_id TYPE bloom_filter() GRANULARITY 1;
2 | ALTER TABLE traces ON CLUSTER default MATERIALIZE INDEX IF EXISTS idx_user_id;
3 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0007_add_event_log.down.sql:
--------------------------------------------------------------------------------
1 | DROP TABLE event_log ON CLUSTER default;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0007_add_event_log.up.sql:
--------------------------------------------------------------------------------
 1 | CREATE TABLE event_log ON CLUSTER default
 2 | (
 3 |     `id`          String,
 4 |     `project_id`  String,
 5 |     `entity_type` String,
 6 |     `entity_id`   String,
 7 |     `event_id`    Nullable(String),
 8 | 
 9 |     `bucket_name` String,
10 |     `bucket_path` String,
11 | 
12 |     `created_at`  DateTime64(3) DEFAULT now(),
13 |     `updated_at`  DateTime64(3) DEFAULT now()
14 | ) ENGINE = MergeTree()
15 |       ORDER BY (
16 |                 project_id,
17 |                 entity_type,
18 |                 entity_id
19 |           );
20 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0008_add_environments_column.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE traces ON CLUSTER default DROP COLUMN IF EXISTS environment;
2 | ALTER TABLE observations ON CLUSTER default DROP COLUMN IF EXISTS environment;
3 | ALTER TABLE scores ON CLUSTER default DROP COLUMN IF EXISTS environment;
4 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0008_add_environments_column.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE traces ON CLUSTER default ADD COLUMN environment LowCardinality(String) DEFAULT 'default' AFTER project_id;
2 | ALTER TABLE observations ON CLUSTER default ADD COLUMN environment LowCardinality(String) DEFAULT 'default' AFTER project_id;
3 | ALTER TABLE scores ON CLUSTER default ADD COLUMN environment LowCardinality(String) DEFAULT 'default' AFTER project_id;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0009_add_project_environments.down.sql:
--------------------------------------------------------------------------------
1 | -- Drop materialized views
2 | DROP VIEW IF EXISTS project_environments_traces_mv ON CLUSTER default;
3 | DROP VIEW IF EXISTS project_environments_observations_mv ON CLUSTER default;
4 | DROP VIEW IF EXISTS project_environments_scores_mv ON CLUSTER default;
5 | 
6 | -- Drop the project_environments table
7 | DROP TABLE IF EXISTS project_environments ON CLUSTER default;
8 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0010_add_metadata_column_on_scores.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default DROP COLUMN IF EXISTS metadata;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0010_add_metadata_column_on_scores.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default ADD COLUMN metadata Map(LowCardinality(String), String) AFTER comment;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0011_add_blob_storage_file_log.down.sql:
--------------------------------------------------------------------------------
1 | DROP TABLE blob_storage_file_log ON CLUSTER default;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0012_add_session_id_column_scores.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default DROP COLUMN IF EXISTS session_id SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0012_add_session_id_column_scores.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default ADD COLUMN session_id Nullable(String) AFTER trace_id SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0013_drop_scores_trace_id_index.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default ADD INDEX IF NOT EXISTS idx_project_trace_observation (project_id, trace_id, observation_id) TYPE bloom_filter(0.001) GRANULARITY 1 SETTINGS mutations_sync = 2;
2 | ALTER TABLE scores ON CLUSTER default MATERIALIZE INDEX IF EXISTS idx_project_trace_observation SETTINGS mutations_sync = 2;
3 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0013_drop_scores_trace_id_index.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default DROP INDEX IF EXISTS idx_project_trace_observation SETTINGS mutations_sync = 2;
2 | 
3 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0014_scores_modify_nullable_trace_id_column.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default MODIFY COLUMN trace_id Nullable(String) SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0014_scores_modify_nullable_trace_id_column.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default MODIFY COLUMN trace_id Nullable(String) SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0015_add_scores_trace_index.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default DROP INDEX IF EXISTS idx_project_trace_observation SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0015_add_scores_trace_index.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default ADD INDEX IF NOT EXISTS idx_project_trace_observation (project_id, trace_id, observation_id) TYPE bloom_filter(0.001) GRANULARITY 1 SETTINGS mutations_sync = 2;
2 | ALTER TABLE scores ON CLUSTER default MATERIALIZE INDEX IF EXISTS idx_project_trace_observation SETTINGS mutations_sync = 2;
3 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0016_add_scores_session_index.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default DROP INDEX IF EXISTS idx_project_session SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0016_add_scores_session_index.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default ADD INDEX IF NOT EXISTS idx_project_session (project_id, session_id) TYPE bloom_filter(0.001) GRANULARITY 1 SETTINGS mutations_sync = 2;
2 | ALTER TABLE scores ON CLUSTER default MATERIALIZE INDEX IF EXISTS idx_project_session SETTINGS mutations_sync = 2;
3 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0017_add_run_id_column_scores.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default DROP COLUMN IF EXISTS dataset_run_id SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0017_add_run_id_column_scores.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default ADD COLUMN dataset_run_id Nullable(String) AFTER session_id SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0018_add_scores_run_index.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default DROP INDEX IF EXISTS idx_project_dataset_run SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0018_add_scores_run_index.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default ADD INDEX IF NOT EXISTS idx_project_dataset_run (project_id, dataset_run_id) TYPE bloom_filter(0.001) GRANULARITY 1 SETTINGS mutations_sync = 2;
2 | ALTER TABLE scores ON CLUSTER default MATERIALIZE INDEX IF EXISTS idx_project_dataset_run SETTINGS mutations_sync = 2;
3 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0019_analytics_traces.down.sql:
--------------------------------------------------------------------------------
1 | DROP VIEW IF EXISTS analytics_traces ON CLUSTER default;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0019_analytics_traces.up.sql:
--------------------------------------------------------------------------------
 1 | CREATE VIEW analytics_traces ON CLUSTER default AS
 2 | SELECT
 3 |     project_id,
 4 |     toStartOfHour(timestamp) AS hour,
 5 |     uniq(id) AS countTraces,
 6 |     max(user_id IS NOT NULL) AS hasUsers,
 7 |     max(session_id IS NOT NULL) AS hasSessions,
 8 |     max(if(environment != 'default', 1, 0)) AS hasEnvironments,
 9 |     max(length(tags) > 0) AS hasTags
10 | FROM
11 |     traces
12 | WHERE toStartOfHour(timestamp) <= toStartOfHour(subtractHours(now(), 1))
13 | GROUP BY
14 |     project_id,
15 |     hour;
16 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0020_analytics_observations.down.sql:
--------------------------------------------------------------------------------
1 | DROP VIEW IF EXISTS analytics_observations ON CLUSTER default;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0021_analytics_scores.down.sql:
--------------------------------------------------------------------------------
1 | DROP VIEW IF EXISTS analytics_scores ON CLUSTER default;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0001_traces.down.sql:
--------------------------------------------------------------------------------
1 | DROP TABLE traces;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0002_observations.down.sql:
--------------------------------------------------------------------------------
1 | DROP TABLE observations;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0003_scores.down.sql:
--------------------------------------------------------------------------------
1 | DROP TABLE scores;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0004_drop_observations_index.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE observations ADD INDEX IF NOT EXISTS idx_project_id project_id TYPE bloom_filter() GRANULARITY 1;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0004_drop_observations_index.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE observations DROP INDEX IF EXISTS idx_project_id;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0005_add_session_id_index.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE traces DROP INDEX IF EXISTS idx_session_id;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0005_add_session_id_index.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE traces ADD INDEX IF NOT EXISTS idx_session_id session_id TYPE bloom_filter() GRANULARITY 1;
2 | ALTER TABLE traces MATERIALIZE INDEX IF EXISTS idx_session_id;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0006_add_user_id_index.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE traces ON CLUSTER default DROP INDEX IF EXISTS idx_user_id;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0006_add_user_id_index.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE traces ADD INDEX IF NOT EXISTS idx_user_id user_id TYPE bloom_filter() GRANULARITY 1;
2 | ALTER TABLE traces MATERIALIZE INDEX IF EXISTS idx_user_id;
3 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0007_add_event_log.down.sql:
--------------------------------------------------------------------------------
1 | DROP TABLE event_log;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0007_add_event_log.up.sql:
--------------------------------------------------------------------------------
 1 | CREATE TABLE event_log
 2 | (
 3 |     `id`          String,
 4 |     `project_id`  String,
 5 |     `entity_type` String,
 6 |     `entity_id`   String,
 7 |     `event_id`    Nullable(String),
 8 | 
 9 |     `bucket_name` String,
10 |     `bucket_path` String,
11 | 
12 |     `created_at`  DateTime64(3) DEFAULT now(),
13 |     `updated_at`  DateTime64(3) DEFAULT now()
14 | ) ENGINE = MergeTree()
15 |       ORDER BY (
16 |                 project_id,
17 |                 entity_type,
18 |                 entity_id
19 |           );
20 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0008_add_environments_column.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE traces DROP COLUMN IF EXISTS environment;
2 | ALTER TABLE observations DROP COLUMN IF EXISTS environment;
3 | ALTER TABLE scores DROP COLUMN IF EXISTS environment;
4 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0008_add_environments_column.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE traces ADD COLUMN environment LowCardinality(String) DEFAULT 'default' AFTER project_id;
2 | ALTER TABLE observations ADD COLUMN environment LowCardinality(String) DEFAULT 'default' AFTER project_id;
3 | ALTER TABLE scores ADD COLUMN environment LowCardinality(String) DEFAULT 'default' AFTER project_id;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0009_add_project_environments.down.sql:
--------------------------------------------------------------------------------
1 | -- Drop materialized views
2 | DROP VIEW IF EXISTS project_environments_traces_mv;
3 | DROP VIEW IF EXISTS project_environments_observations_mv;
4 | DROP VIEW IF EXISTS project_environments_scores_mv;
5 | 
6 | -- Drop the project_environments table
7 | DROP TABLE IF EXISTS project_environments;
8 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0010_add_metadata_column_on_scores.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores DROP COLUMN IF EXISTS metadata;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0010_add_metadata_column_on_scores.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ADD COLUMN metadata Map(LowCardinality(String), String) AFTER comment;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0011_add_blob_storage_file_log.down.sql:
--------------------------------------------------------------------------------
1 | DROP TABLE blob_storage_file_log;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0012_add_session_id_column_scores.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores DROP COLUMN IF EXISTS session_id SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0012_add_session_id_column_scores.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ADD COLUMN session_id Nullable(String) AFTER trace_id SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0013_drop_scores_trace_id_index.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ADD INDEX IF NOT EXISTS idx_project_trace_observation (project_id, trace_id, observation_id) TYPE bloom_filter(0.001) GRANULARITY 1 SETTINGS mutations_sync = 2;
2 | ALTER TABLE scores MATERIALIZE INDEX IF EXISTS idx_project_trace_observation SETTINGS mutations_sync = 2;
3 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0013_drop_scores_trace_id_index.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores DROP INDEX IF EXISTS idx_project_trace_observation SETTINGS mutations_sync = 2;
2 | 
3 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0014_scores_modify_nullable_trace_id_column.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores MODIFY COLUMN trace_id Nullable(String) SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0014_scores_modify_nullable_trace_id_column.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores MODIFY COLUMN trace_id Nullable(String) SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0015_add_scores_trace_index.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores DROP INDEX IF EXISTS idx_project_trace_observation SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0015_add_scores_trace_index.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ADD INDEX IF NOT EXISTS idx_project_trace_observation (project_id, trace_id, observation_id) TYPE bloom_filter(0.001) GRANULARITY 1 SETTINGS mutations_sync = 2; 
2 | ALTER TABLE scores MATERIALIZE INDEX IF EXISTS idx_project_trace_observation SETTINGS mutations_sync = 2;
3 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0016_add_scores_session_index.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores DROP INDEX IF EXISTS idx_project_session SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0016_add_scores_session_index.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ADD INDEX IF NOT EXISTS idx_project_session (project_id, session_id) TYPE bloom_filter(0.001) GRANULARITY 1 SETTINGS mutations_sync = 2;
2 | ALTER TABLE scores MATERIALIZE INDEX IF EXISTS idx_project_session SETTINGS mutations_sync = 2;
3 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0017_add_run_id_column_scores.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores DROP COLUMN IF EXISTS dataset_run_id SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0017_add_run_id_column_scores.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ADD COLUMN dataset_run_id Nullable(String) AFTER session_id SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0018_add_scores_run_index.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores DROP INDEX IF EXISTS idx_project_dataset_run SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0018_add_scores_run_index.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ADD INDEX IF NOT EXISTS idx_project_dataset_run (project_id, dataset_run_id) TYPE bloom_filter(0.001) GRANULARITY 1 SETTINGS mutations_sync = 2;
2 | ALTER TABLE scores MATERIALIZE INDEX IF EXISTS idx_project_dataset_run SETTINGS mutations_sync = 2;
3 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0019_analytics_traces.down.sql:
--------------------------------------------------------------------------------
1 | DROP VIEW IF EXISTS analytics_traces;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0019_analytics_traces.up.sql:
--------------------------------------------------------------------------------
 1 | CREATE VIEW analytics_traces AS
 2 | SELECT
 3 |     project_id,
 4 |     toStartOfHour(timestamp) AS hour,
 5 |     uniq(id) AS countTraces,
 6 |     max(user_id IS NOT NULL) AS hasUsers,
 7 |     max(session_id IS NOT NULL) AS hasSessions,
 8 |     max(if(environment != 'default', 1, 0)) AS hasEnvironments,
 9 |     max(length(tags) > 0) AS hasTags
10 | FROM
11 |     traces
12 | WHERE toStartOfHour(timestamp) <= toStartOfHour(subtractHours(now(), 1))
13 | GROUP BY
14 |     project_id,
15 |     hour;
16 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0020_analytics_observations.down.sql:
--------------------------------------------------------------------------------
1 | DROP VIEW IF EXISTS analytics_observations;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0021_analytics_scores.down.sql:
--------------------------------------------------------------------------------
1 | DROP VIEW IF EXISTS analytics_scores;
2 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230522094431_endtime_optional/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "observations" ALTER COLUMN "end_time" DROP NOT NULL;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230522131516_default_timestamp/migration.sql:
--------------------------------------------------------------------------------
 1 | /*
 2 |   Warnings:
 3 | 
 4 |   - You are about to drop the column `createdAt` on the `metrics` table. All the data in the column will be lost.
 5 | 
 6 | */
 7 | -- AlterTable
 8 | ALTER TABLE "metrics" DROP COLUMN "createdAt",
 9 | ADD COLUMN     "timestamp" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP;
10 | 
11 | -- AlterTable
12 | ALTER TABLE "observations" ALTER COLUMN "start_time" SET DEFAULT CURRENT_TIMESTAMP;
13 | 
14 | -- AlterTable
15 | ALTER TABLE "traces" ALTER COLUMN "timestamp" SET DEFAULT CURRENT_TIMESTAMP;
16 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230529140133_user_add_pw/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "User" ADD COLUMN     "password" TEXT;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230618125818_remove_status_from_trace/migration.sql:
--------------------------------------------------------------------------------
 1 | /*
 2 |   Warnings:
 3 | 
 4 |   - You are about to drop the column `status` on the `traces` table. All the data in the column will be lost.
 5 |   - You are about to drop the column `status_message` on the `traces` table. All the data in the column will be lost.
 6 | 
 7 | */
 8 | -- AlterTable
 9 | ALTER TABLE "traces" DROP COLUMN "status",
10 | DROP COLUMN "status_message";
11 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230622114254_new_oservations/migration.sql:
--------------------------------------------------------------------------------
 1 | BEGIN;
 2 | 
 3 | ALTER TABLE "observations"
 4 | RENAME COLUMN "prompt" TO "input";
 5 | 
 6 | ALTER TABLE "observations"
 7 | ADD COLUMN "output_temp" JSONB;
 8 | 
 9 | UPDATE "observations"
10 | SET "output_temp" = json_build_object('completion', "observations"."completion");
11 | 
12 | ALTER TABLE "observations"
13 | DROP COLUMN "completion";
14 | 
15 | ALTER TABLE "observations"
16 | RENAME COLUMN "output_temp" TO "output";
17 | 
18 | COMMIT;


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230623172401_observation_add_level_and_status_message/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateEnum
2 | CREATE TYPE "ObservationLevel" AS ENUM ('DEBUG', 'DEFAULT', 'WARNING', 'ERROR');
3 | 
4 | -- AlterTable
5 | ALTER TABLE "observations" ADD COLUMN     "level" "ObservationLevel" NOT NULL DEFAULT 'DEFAULT',
6 | ADD COLUMN     "status_message" TEXT;
7 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230626095337_external_trace_id/migration.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE "traces" ADD COLUMN     "external_id" TEXT;
2 | CREATE UNIQUE INDEX "traces_project_id_external_id_key" ON "traces"("project_id", "external_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230705160335_add_created_updated_timestamps/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "memberships" ADD COLUMN     "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
3 | ADD COLUMN     "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP;
4 | 
5 | -- AlterTable
6 | ALTER TABLE "users" ADD COLUMN     "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
7 | ADD COLUMN     "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP;
8 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230706195819_add_completion_start_time/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "observations" ADD COLUMN     "completion_start_time" TIMESTAMP(3);
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230707132314_traces_project_id_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX "traces_project_id_idx" ON "traces"("project_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230707133415_user_add_email_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX "Account_user_id_idx" ON "Account"("user_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230710105741_added_indices/migration.sql:
--------------------------------------------------------------------------------
 1 | -- DropIndex
 2 | DROP INDEX "traces_project_id_idx";
 3 | 
 4 | -- CreateIndex
 5 | CREATE INDEX "observations_trace_id_type_idx" ON "observations"("trace_id", "type");
 6 | 
 7 | -- CreateIndex
 8 | CREATE INDEX "scores_value_idx" ON "scores"("value");
 9 | 
10 | -- CreateIndex
11 | CREATE INDEX "traces_project_id_name_idx" ON "traces"("project_id", "name");
12 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230710114928_traces_add_user_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | DROP INDEX "traces_project_id_name_idx";
3 | 
4 | -- AlterTable
5 | ALTER TABLE "traces" ADD COLUMN     "user_id" TEXT;
6 | 
7 | -- CreateIndex
8 | CREATE INDEX "traces_project_id_name_user_id_idx" ON "traces"("project_id", "name", "user_id");
9 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230710200816_scores_add_comment/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "scores" ADD COLUMN     "comment" TEXT;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230711104810_traces_add_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | DROP INDEX "traces_project_id_name_user_id_idx";
3 | 
4 | -- CreateIndex
5 | CREATE INDEX "traces_project_id_name_user_id_external_id_idx" ON "traces"("project_id", "name", "user_id", "external_id");
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230711110517_memberships_add_userid_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX "memberships_user_id_idx" ON "memberships"("user_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230717190411_users_feature_flags/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "users" ADD COLUMN     "feature_flags" TEXT[] DEFAULT ARRAY[]::TEXT[];
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230720162550_tokens/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "observations" ADD COLUMN     "completion_tokens" INTEGER,
3 | ADD COLUMN     "prompt_tokens" INTEGER,
4 | ADD COLUMN     "total_tokens" INTEGER;
5 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230720164603_migrate_tokens/migration.sql:
--------------------------------------------------------------------------------
1 | -- This is an empty migration.
2 | UPDATE observations
3 |   SET prompt_tokens = CAST(usage::json->>'promptTokens' AS INTEGER),
4 |   completion_tokens = CAST(usage::json->>'completionTokens' AS INTEGER),
5 |   total_tokens = CAST(usage::json->>'totalTokens' AS INTEGER);


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230721111651_drop_usage_json/migration.sql:
--------------------------------------------------------------------------------
1 | /*
2 |   Warnings:
3 | 
4 |   - You are about to drop the column `usage` on the `observations` table. All the data in the column will be lost.
5 | 
6 | */
7 | -- AlterTable
8 | ALTER TABLE "observations" DROP COLUMN "usage";
9 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230731162154_score_value_float/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "scores" ALTER COLUMN "value" SET DATA TYPE DOUBLE PRECISION;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230803093326_add_release_and_version/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "observations" ADD COLUMN     "version" TEXT;
3 | 
4 | -- AlterTable
5 | ALTER TABLE "traces" ADD COLUMN     "release" TEXT,
6 | ADD COLUMN     "version" TEXT;
7 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230809093636_remove_foreign_keys/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropForeignKey
2 | ALTER TABLE "observations" DROP CONSTRAINT "observations_parent_observation_id_fkey";
3 | 
4 | -- DropForeignKey
5 | ALTER TABLE "observations" DROP CONSTRAINT "observations_trace_id_fkey";
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230810191452_traceid_nullable_on_observations/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "observations" ALTER COLUMN "trace_id" DROP NOT NULL;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230810191453_project_id_not_null/migration.sql:
--------------------------------------------------------------------------------
1 | -- Applied in separate migration after application release to minimize ingestion downtime
2 | ALTER TABLE "observations"
3 | ALTER COLUMN "project_id" SET NOT NULL;
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230814184705_add_viewer_membership_role/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterEnum
2 | ALTER TYPE "MembershipRole" ADD VALUE 'VIEWER';
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230901155252_add_pricings_table/migration.sql:
--------------------------------------------------------------------------------
 1 | -- CreateEnum
 2 | CREATE TYPE "PricingUnit" AS ENUM ('PER_1000_TOKENS');
 3 | 
 4 | -- CreateEnum
 5 | CREATE TYPE "TokenType" AS ENUM ('PROMPT', 'COMPLETION', 'TOTAL');
 6 | 
 7 | -- CreateTable
 8 | CREATE TABLE "pricings" (
 9 |     "id" TEXT NOT NULL,
10 |     "model_name" TEXT NOT NULL,
11 |     "pricing_unit" "PricingUnit" NOT NULL DEFAULT 'PER_1000_TOKENS',
12 |     "price" DECIMAL(65,30) NOT NULL,
13 |     "currency" TEXT NOT NULL DEFAULT 'USD',
14 |     "token_type" "TokenType" NOT NULL,
15 | 
16 |     CONSTRAINT "pricings_pkey" PRIMARY KEY ("id")
17 | );
18 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230907204921_add_cron_jobs_table/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateTable
2 | CREATE TABLE "cron_jobs" (
3 |     "name" TEXT NOT NULL,
4 |     "last_run" TIMESTAMP(3),
5 | 
6 |     CONSTRAINT "cron_jobs_pkey" PRIMARY KEY ("name")
7 | );
8 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230907225603_projects_updated_at/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "projects" ADD COLUMN     "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230907225604_api_keys_publishable_to_public/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | DROP INDEX "api_keys_publishable_key_key";
3 | 
4 | -- RENAME column from "publishable_key" to "public_key" on table "api_keys"
5 | ALTER TABLE "api_keys" rename column "publishable_key" to "public_key";
6 | 
7 | -- CreateIndex
8 | CREATE UNIQUE INDEX "api_keys_public_key_key" ON "api_keys"("public_key");
9 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230910164603_cron_add_state/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "cron_jobs" ADD COLUMN     "state" TEXT;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230912115644_add_trace_public_bool/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "traces" ADD COLUMN     "public" BOOLEAN NOT NULL DEFAULT false;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230918180320_add_indices/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX "observations_start_time_idx" ON "observations"("start_time");
3 | 
4 | -- CreateIndex
5 | CREATE INDEX "traces_timestamp_idx" ON "traces"("timestamp");
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230922030325_add_observation_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX "observations_project_id_idx" ON "observations"("project_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231004005909_add_parent_observation_id_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX "observations_parent_observation_id_idx" ON "observations"("parent_observation_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231005064433_add_release_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX "traces_release_idx" ON "traces"("release");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231012161041_add_events_table/migration.sql:
--------------------------------------------------------------------------------
 1 | -- CreateTable
 2 | CREATE TABLE "events" (
 3 |     "id" TEXT NOT NULL,
 4 |     "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
 5 |     "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
 6 |     "project_id" TEXT NOT NULL,
 7 |     "data" JSONB NOT NULL,
 8 |     "url" TEXT,
 9 |     "method" TEXT,
10 | 
11 |     CONSTRAINT "events_pkey" PRIMARY KEY ("id")
12 | );
13 | 
14 | -- AddForeignKey
15 | ALTER TABLE "events" ADD CONSTRAINT "events_project_id_fkey" FOREIGN KEY ("project_id") REFERENCES "projects"("id") ON DELETE CASCADE ON UPDATE CASCADE;
16 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231014131841_users_add_admin_flag/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "users" ADD COLUMN     "admin" BOOLEAN NOT NULL DEFAULT false;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231018130032_add_per_1000_chars_pricing/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterEnum
2 | ALTER TYPE "PricingUnit" ADD VALUE 'PER_1000_CHARS';
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231021182825_user_emails_all_lowercase/migration.sql:
--------------------------------------------------------------------------------
1 | -- Due to the unique constraint on the email column, we need to make sure that all emails are in lowercase.
2 | -- This migration will update all existing emails to be lowercase.
3 | -- This migration fails if there are duplicate emails in the database.
4 | 
5 | UPDATE "users" SET "email" = LOWER("email");
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231025153548_add_headers_to_events/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "events" ADD COLUMN     "headers" JSONB NOT NULL DEFAULT '{}';
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231030184329_events_add_index_on_projectid/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX "events_project_id_idx" ON "events"("project_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231104004529_scores_add_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX "scores_trace_id_idx" ON "scores" USING HASH ("trace_id");
3 | 
4 | -- CreateIndex
5 | CREATE INDEX "scores_observation_id_idx" ON "scores" USING HASH ("observation_id");
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231106213824_add_openai_models/migration.sql:
--------------------------------------------------------------------------------
 1 | -- This is an empty migration.
 2 | 
 3 | INSERT INTO pricings (
 4 |   id,
 5 |   model_name, 
 6 |   pricing_unit, 
 7 |   price,
 8 |   currency,
 9 |   token_type
10 | )
11 | VALUES
12 |   ('clm0obv1u00003b6lc2etkzfu','gpt-4-1106-preview', 'PER_1000_TOKENS', 0.01, 'USD', 'PROMPT'),
13 |   ('clm0obv1u00003b6lc2etkzfg','gpt-4-1106-preview', 'PER_1000_TOKENS', 0.03, 'USD', 'COMPLETION'),
14 |   ('clm0obv1u00013b6l4gdl83vs','gpt-4-1106-vision-preview	', 'PER_1000_TOKENS', 0.01, 'USD', 'PROMPT'),
15 |   ('clm0obv1u00013b6l4gjl83vs','gpt-4-1106-vision-preview	', 'PER_1000_TOKENS', 0.03, 'USD', 'COMPLETION')


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231110012457_observation_created_at/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "observations" ADD COLUMN "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231110012829_observation_created_at_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX "observations_created_at_idx" ON "observations"("created_at");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231112095703_observations_add_unique_constraint/migration.sql:
--------------------------------------------------------------------------------
1 | /*
2 |   Warnings:
3 | 
4 |   - A unique constraint covering the columns `[id,project_id]` on the table `observations` will be added. If there are existing duplicate values, this will fail.
5 | 
6 | */
7 | -- CreateIndex
8 | CREATE UNIQUE INDEX "observations_id_project_id_key" ON "observations"("id", "project_id");
9 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231116005353_scores_unique_id_projectid/migration.sql:
--------------------------------------------------------------------------------
1 | /*
2 |   Warnings:
3 | 
4 |   - A unique constraint covering the columns `[id,trace_id]` on the table `scores` will be added. If there are existing duplicate values, this will fail.
5 | 
6 | */
7 | -- CreateIndex
8 | CREATE UNIQUE INDEX "scores_id_trace_id_key" ON "scores"("id", "trace_id");
9 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231119171939_cron_add_job_started_at/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "cron_jobs" ADD COLUMN     "job_started_at" TIMESTAMP(3);
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231119171940_bookmarked/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- AlterTable
3 | ALTER TABLE "traces" ADD COLUMN "bookmarked" BOOLEAN NOT NULL DEFAULT false;
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231204223505_add_unit_to_observations/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | -- Adding this migration does not lock the postgres table. For non volaitile data, the default value is stored in the 
3 | -- table metadata and accessed on read query time. No table re-write is required (https://www.postgresql.org/docs/current/sql-altertable.html#:~:text=When%20a%20column%20is%20added,is%20specified%2C%20NULL%20is%20used.)
4 | ALTER TABLE "observations" ADD COLUMN "unit" TEXT NOT NULL DEFAULT 'TOKENS';


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231223230007_cloud_config/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "projects" ADD COLUMN     "cloud_config" JSONB;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231223230008_accounts_add_cols_azure_ad_auth/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "Account" ADD COLUMN     "expires_in" INTEGER,
3 | ADD COLUMN     "ext_expires_in" INTEGER;
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240104210051_add_model_indices/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "observations_model_idx" ON "observations"("model");
3 | 
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240104210052_add_model_indices_pricing/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "pricings_model_name_idx" ON "pricings"("model_name");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240105010215_add_tags_in_traces/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "traces" ADD COLUMN     "tags" TEXT[] DEFAULT ARRAY[]::TEXT[];
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240105170551_index_tags_in_traces/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX "traces_tags_idx" ON "traces" USING GIN ("tags" array_ops);
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240106195340_drop_dataset_status/migration.sql:
--------------------------------------------------------------------------------
1 | /*
2 |   Warnings:
3 | 
4 |   - You are about to drop the column `status` on the `datasets` table. All the data in the column will be lost.
5 | 
6 | */
7 | -- AlterTable
8 | ALTER TABLE "datasets" DROP COLUMN "status";
9 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240111152124_add_gpt_35_pricing/migration.sql:
--------------------------------------------------------------------------------
 1 | -- Migration to add gpt-35 spelling
 2 | 
 3 | INSERT INTO pricings (
 4 |   id,
 5 |   model_name, 
 6 |   pricing_unit, 
 7 |   price,
 8 |   currency,
 9 |   token_type
10 | )
11 | VALUES
12 |   ('clqqpc2pr000008l3hvy63gxy1','gpt-35-turbo-1106', 'PER_1000_TOKENS', 0.001, 'USD', 'PROMPT'),
13 |   ('clqqpcb6d000208l3atrfbmou1','gpt-35-turbo-1106', 'PER_1000_TOKENS', 0.002, 'USD', 'COMPLETION'),
14 |   ('clqqpdh45000008lfgrnx76cv1','gpt-35-turbo-instruct', 'PER_1000_TOKENS', 0.0015, 'USD', 'PROMPT'),
15 |   ('clqqpdjya000108lf3s4b4c4m1','gpt-35-turbo-instruct', 'PER_1000_TOKENS', 0.002, 'USD', 'COMPLETION')
16 | ON CONFLICT (id) DO NOTHING;


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240117151938_traces_remove_unique_id_external/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | DROP INDEX "traces_project_id_external_id_key";
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240117165747_add_cost_to_observations/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "observations" ADD COLUMN     "input_cost" DECIMAL(65,30),
3 | ADD COLUMN     "output_cost" DECIMAL(65,30),
4 | ADD COLUMN     "total_cost" DECIMAL(65,30);
5 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240118204936_add_internal_model/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "observations" ADD COLUMN     "internal_model" TEXT;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240118235424_add_index_to_models/migration.sql:
--------------------------------------------------------------------------------
 1 | /*
 2 |   Warnings:
 3 | 
 4 |   - A unique constraint covering the columns `[project_id,model_name,start_date,unit]` on the table `models` will be added. If there are existing duplicate values, this will fail.
 5 | 
 6 | */
 7 | -- CreateIndex
 8 | CREATE INDEX "models_project_id_model_name_idx" ON "models"("project_id", "model_name");
 9 | 
10 | -- CreateIndex
11 | CREATE UNIQUE INDEX "models_project_id_model_name_start_date_unit_key" ON "models"("project_id", "model_name", "start_date", "unit");
12 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240119140941_add_tokenizer_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "models" ADD COLUMN     "tokenizer_id" TEXT;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240119164147_make_model_params_nullable/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "models" ALTER COLUMN "tokenizer_config" DROP NOT NULL;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240130100110_usage_unit_nullable/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "models" ALTER COLUMN "unit" DROP DEFAULT;
3 | 
4 | -- AlterTable
5 | ALTER TABLE "observations" ALTER COLUMN "unit" DROP NOT NULL,
6 | ALTER COLUMN "unit" DROP DEFAULT;
7 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240214232619_prompts_add_indicies/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX "prompts_project_id_id_idx" ON "prompts"("project_id", "id");
3 | 
4 | -- CreateIndex
5 | CREATE INDEX "prompts_project_id_idx" ON "prompts"("project_id");
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240215224148_update_openai_pricing/migration.sql:
--------------------------------------------------------------------------------
 1 | -- This is an empty migration.
 2 | 
 3 | INSERT INTO models (
 4 |   id,
 5 |   project_id,
 6 |   model_name,
 7 |   match_pattern,
 8 |   start_date,
 9 |   input_price,
10 |   output_price,
11 |   total_price,
12 |   unit,
13 |   tokenizer_id,
14 |   tokenizer_config
15 | )
16 | VALUES
17 |   ('clsnq07bn000008l4e46v1ll8', NULL, 'gpt-4-turbo-preview', '(?i)^(gpt-4-turbo-preview)
#39;, '2023-11-06', 0.00001, 0.00003, NULL, 'TOKENS', 'openai', '{ "tokensPerMessage": 3, "tokensPerName": 1, "tokenizerModel": "gpt-4" }')


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240219162415_add_prompt_config/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "prompts" ADD COLUMN     "config" JSONB NOT NULL DEFAULT '{}';
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240226165118_add_observations_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "observations_project_id_start_time_type_idx" ON "observations"("project_id", "start_time", "type");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240226182815_add_model_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "models_project_id_model_name_start_date_unit_idx" ON "models"("project_id", "model_name", "start_date", "unit");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240226183642_add_observations_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "observations_project_id_internal_model_start_time_unit_idx" ON "observations"("project_id", "internal_model", "start_time", "unit");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240226202040_add_observations_trace_id_project_id_start_time_idx/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "observations_trace_id_project_id_start_time_idx" ON "observations"("trace_id", "project_id", "start_time");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240226202041_add_observations_trace_id_project_id_type_start_time_idx/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "observations_trace_id_project_id_type_start_time_idx" ON "observations"("trace_id", "project_id", "type", "start_time");


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240227112101_index_prompt_id_in_observations/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY IF NOT EXISTS "observations_prompt_id_idx" ON "observations"("prompt_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240304123642_traces_view/migration.sql:
--------------------------------------------------------------------------------
1 | CREATE VIEW trace_metrics_view AS
2 | SELECT
3 |     t.id,
4 |     EXTRACT(EPOCH FROM COALESCE(MAX(o.end_time), MAX(o.start_time))) - EXTRACT(EPOCH FROM MIN(o.start_time))::double precision AS duration
5 | FROM
6 |     traces t
7 |     LEFT JOIN observations o ON t.id = o.trace_id
8 | group by t.project_id, t.id


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240304123642_traces_view_improvement/migration.sql:
--------------------------------------------------------------------------------
 1 | DROP VIEW trace_metrics_view;
 2 | 
 3 | 
 4 | CREATE OR REPLACE VIEW traces_view AS
 5 | WITH observations_metrics AS (
 6 |     SELECT
 7 |         trace_id,
 8 |         project_id,
 9 |         EXTRACT(EPOCH FROM COALESCE(MAX(o.end_time), MAX(o.start_time))) - EXTRACT(EPOCH FROM MIN(o.start_time))::double precision AS duration
10 |     FROM
11 |         observations o
12 |     GROUP BY
13 |         project_id, trace_id
14 | )
15 | SELECT
16 |     t.*,
17 |     o.duration
18 | FROM
19 |     traces t
20 |     LEFT JOIN observations_metrics o ON t.id = o.trace_id and t.project_id = o.project_id


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240304222519_scores_add_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "scores_timestamp_idx" ON "scores"("timestamp");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240305095119_add_observations_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "observations_trace_id_project_id_idx" ON "observations"("trace_id", "project_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240305100713_traces_add_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "traces_id_user_id_idx" ON "traces"("id", "user_id");


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240307185543_score_add_source_nullable/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateEnum
2 | CREATE TYPE "ScoreSource" AS ENUM ('API', 'REVIEW');
3 | 
4 | -- AlterTable
5 | ALTER TABLE "scores" ADD COLUMN     "source" "ScoreSource" NOT NULL DEFAULT 'API';
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240307185544_score_add_name_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "scores_source_idx" ON "scores"("source");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240307185725_backfill_score_source/migration.sql:
--------------------------------------------------------------------------------
1 | -- scores previously created in the Langfuse UI all had the name 'manual-score'
2 | UPDATE "scores"
3 | SET "source" = 'REVIEW'::"ScoreSource"
4 | WHERE "name" = 'manual-score';
5 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240312195727_score_source_drop_default/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "scores" ALTER COLUMN "source" DROP DEFAULT;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240314090110_claude_model/migration.sql:
--------------------------------------------------------------------------------
 1 | INSERT INTO models (
 2 |   id,
 3 |   project_id,
 4 |   model_name,
 5 |   match_pattern,
 6 |   start_date,
 7 |   input_price,
 8 |   output_price,
 9 |   total_price,
10 |   unit,
11 |   tokenizer_id,
12 |   tokenizer_config
13 | )
14 | VALUES
15 |   -- https://docs.anthropic.com/claude/docs/models-overview, https://docs.anthropic.com/claude/docs/quickstart-guide
16 |   ('cltr0w45b000008k1407o9qv1', NULL, 'claude-3-haiku-20240307', '(?i)^(claude-3-haiku-20240307)
#39;, NULL, 0.00000025, 0.00000125, NULL, 'TOKENS', 'claude', NULL)
17 | 
18 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240325211959_remove_example_table/migration.sql:
--------------------------------------------------------------------------------
1 | /*
2 |   Warnings:
3 | 
4 |   - You are about to drop the `Example` table. If the table is not empty, all the data it contains will be lost.
5 | 
6 | */
7 | -- DropTable
8 | DROP TABLE "Example";
9 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240325212245_dataset_runs_add_metadata/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "dataset_runs" ADD COLUMN     "metadata" JSONB;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240326114211_dataset_run_item_bind_to_trace/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "dataset_run_items" ADD COLUMN     "trace_id" TEXT,
3 | ALTER COLUMN "observation_id" DROP NOT NULL;
4 | 
5 | -- AddForeignKey
6 | ALTER TABLE "dataset_run_items" ADD CONSTRAINT "dataset_run_items_trace_id_fkey" FOREIGN KEY ("trace_id") REFERENCES "traces"("id") ON DELETE CASCADE ON UPDATE CASCADE;
7 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240326114337_dataset_run_item_backfill_trace_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- Backfill trace_id for existing run_items based on the linked observation
2 | UPDATE dataset_run_items
3 | SET trace_id = observations.trace_id
4 | FROM observations 
5 | WHERE dataset_run_items.observation_id = observations.id;


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240326115136_dataset_run_item_traceid_non_null/migration.sql:
--------------------------------------------------------------------------------
1 | /*
2 |   Warnings:
3 | 
4 |   - Made the column `trace_id` on table `dataset_run_items` required. This step will fail if there are existing NULL values in that column.
5 | 
6 | */
7 | -- AlterTable
8 | ALTER TABLE "dataset_run_items" ALTER COLUMN "trace_id" SET NOT NULL;
9 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240326115424_dataset_run_item_index_trace/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "dataset_run_items_trace_id_idx" ON "dataset_run_items"("trace_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240328065738_dataset_item_input_nullable/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "dataset_items" ALTER COLUMN "input" DROP NOT NULL;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240404203640_dataset_item_source_trace_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "dataset_items" ADD COLUMN     "source_trace_id" TEXT;
3 | 
4 | -- AddForeignKey
5 | ALTER TABLE "dataset_items" ADD CONSTRAINT "dataset_items_source_trace_id_fkey" FOREIGN KEY ("source_trace_id") REFERENCES "traces"("id") ON DELETE SET NULL ON UPDATE CASCADE;
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240404210315_dataset_add_descriptions/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "dataset_runs" ADD COLUMN     "description" TEXT;
3 | 
4 | -- AlterTable
5 | ALTER TABLE "datasets" ADD COLUMN     "description" TEXT;
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240404232317_dataset_items_backfill_source_trace_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- Backfill source_trace_id for existing dataset_items based on the linked source_observation_id
2 | UPDATE dataset_items
3 | SET source_trace_id = observations.trace_id
4 | FROM observations
5 | WHERE dataset_items.source_observation_id = observations.id
6 |   AND dataset_items.source_observation_id IS NOT NULL
7 |   AND dataset_items.source_trace_id IS NULL


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240405124810_prompt_to_json/migration.sql:
--------------------------------------------------------------------------------
 1 | BEGIN;
 2 | 
 3 | ALTER TABLE prompts
 4 | ADD COLUMN json_prompt JSONB;
 5 | 
 6 | UPDATE prompts
 7 | SET json_prompt = to_json(prompt::text)::json;
 8 | 
 9 | ALTER TABLE prompts
10 | DROP COLUMN prompt;
11 | 
12 | ALTER TABLE prompts
13 | RENAME COLUMN json_prompt TO prompt;
14 | 
15 | ALTER TABLE prompts
16 | ALTER COLUMN prompt SET NOT NULL;
17 | 
18 | ALTER TABLE prompts
19 | ADD COLUMN type TEXT NOT NULL DEFAULT 'text';
20 | 
21 | COMMIT;
22 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240408134328_prompt_table_add_tags/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "prompts" ADD COLUMN     "tags" TEXT[] DEFAULT ARRAY[]::TEXT[];
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240408134330_prompt_table_add_index_to_tags/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "prompts_tags_idx" ON "prompts" USING GIN ("tags" array_ops);
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240411194142_update_job_config_status/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateEnum
2 | CREATE TYPE "JobConfigState" AS ENUM ('ACTIVE', 'INACTIVE');
3 | 
4 | -- AlterTable
5 | ALTER TABLE "job_configurations" ADD COLUMN     "status" "JobConfigState" NOT NULL DEFAULT 'ACTIVE';
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240411224142_update_models/migration.sql:
--------------------------------------------------------------------------------
 1 | INSERT INTO models (
 2 |   id,
 3 |   project_id,
 4 |   model_name,
 5 |   match_pattern,
 6 |   start_date,
 7 |   input_price,
 8 |   output_price,
 9 |   total_price,
10 |   unit,
11 |   tokenizer_id,
12 |   tokenizer_config
13 | )
14 | VALUES
15 |   -- https://platform.openai.com/docs/models/continuous-model-upgrades
16 |   ('cluvpl4ls000008l6h2gx3i07', NULL, 'gpt-4-turbo', '(?i)^(gpt-4-turbo)
#39;, NULL, 0.00001, 0.00003, NULL, 'TOKENS', 'openai', '{ "tokensPerMessage": 3, "tokensPerName": 1, "tokenizerModel": "gpt-4-1106-preview" }')


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240414203636_ee_add_sso_configs/migration.sql:
--------------------------------------------------------------------------------
 1 | -- CreateTable
 2 | CREATE TABLE "sso_configs" (
 3 |     "domain" TEXT NOT NULL,
 4 |     "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
 5 |     "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
 6 |     "auth_provider" TEXT NOT NULL,
 7 |     "auth_config" JSONB,
 8 | 
 9 |     CONSTRAINT "sso_configs_pkey" PRIMARY KEY ("domain")
10 | );
11 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240415235737_index_models_model_name/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "models_model_name_idx" ON "models"("model_name");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240416173813_add_internal_model_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "observations_internal_model_idx" ON "observations"("internal_model");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240417102742_metadata_on_dataset_and_dataset_item/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "dataset_items" ADD COLUMN     "metadata" JSONB;
3 | 
4 | -- AlterTable
5 | ALTER TABLE "datasets" ADD COLUMN     "metadata" JSONB;
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240420134232_posthog_integration_created_at/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "posthog_integrations" ADD COLUMN     "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240424150909_add_job_execution_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX "job_executions_project_id_status_idx" ON "job_executions"("project_id", "status");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240429124411_add_prompt_version_labels/migration.sql:
--------------------------------------------------------------------------------
 1 | BEGIN;
 2 | 
 3 | -- Step 1: Alter the 'prompts' table to add the 'labels' column
 4 | ALTER TABLE prompts
 5 | ADD COLUMN labels TEXT[] DEFAULT ARRAY[]::TEXT[];
 6 | 
 7 | -- Step 2: Update the 'labels' column to include 'production' for active prompts
 8 | UPDATE prompts
 9 | SET labels = array_append(labels, 'production')
10 | WHERE is_active = TRUE;
11 | 
12 | -- Step 3: Drop the required constraint on 'is_active' column.
13 | ALTER TABLE prompts
14 | ALTER COLUMN is_active DROP NOT NULL;
15 | 
16 | COMMIT;


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240429194411_add_latest_prompt_tag/migration.sql:
--------------------------------------------------------------------------------
 1 | UPDATE
 2 | 	prompts
 3 | SET
 4 | 	labels = array_append(labels, 'latest')
 5 | WHERE
 6 | 	id = (
 7 | 		SELECT
 8 | 			id
 9 | 		FROM
10 | 			prompts AS p2
11 | 		WHERE
12 | 			p2.name = prompts.name
13 | 		ORDER BY
14 | 			created_at DESC
15 | 		LIMIT 1);


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240503125742_traces_add_createdat_updatedat/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "traces" ADD COLUMN     "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
3 | ADD COLUMN     "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP;
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240503130335_traces_index_created_at/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | 
3 | CREATE INDEX CONCURRENTLY "traces_created_at_idx" ON "traces"("created_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240503130520_traces_index_updated_at/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | 
3 | CREATE INDEX CONCURRENTLY "traces_updated_at_idx" ON "traces"("updated_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240508132621_scores_add_project_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "scores" ADD COLUMN     "project_id" TEXT;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240508132735_scores_add_projectid_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "scores_project_id_idx" ON "scores"("project_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240508132736_scores_backfill_project_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- Backfill project_id on existing scores based on linked trace_id
2 | UPDATE scores
3 | SET project_id = traces.project_id
4 | FROM traces 
5 | WHERE scores.trace_id = traces.id AND scores.project_id IS NULL;
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240512155021_scores_drop_fk_on_traces_and_observations/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropForeignKey
2 | ALTER TABLE "scores" DROP CONSTRAINT "scores_observation_id_fkey";
3 | 
4 | -- DropForeignKey
5 | ALTER TABLE "scores" DROP CONSTRAINT "scores_trace_id_fkey";
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240512155022_scores_non_null_and_add_fk_project_id/migration.sql:
--------------------------------------------------------------------------------
 1 | /*
 2 |   Warnings:
 3 | 
 4 |   - Made the column `project_id` on table `scores` required. This step will fail if there are existing NULL values in that column.
 5 | 
 6 | */
 7 | -- AlterTable
 8 | ALTER TABLE "scores" ALTER COLUMN "project_id" SET NOT NULL;
 9 | 
10 | -- AddForeignKey
11 | ALTER TABLE "scores" ADD CONSTRAINT "scores_project_id_fkey" FOREIGN KEY ("project_id") REFERENCES "projects"("id") ON DELETE CASCADE ON UPDATE CASCADE;
12 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240513082203_scores_unique_id_and_projectid_instead_of_id_and_traceid/migration.sql:
--------------------------------------------------------------------------------
1 | /*
2 |   Warnings:
3 | 
4 |   - A unique constraint covering the columns `[id,project_id]` on the table `scores` will be added. If there are existing duplicate values, this will fail.
5 | 
6 | */
7 | -- DropIndex
8 | DROP INDEX "scores_id_trace_id_key";
9 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240513082204_scores_unique_id_and_projectid_instead_of_id_and_traceid_index/migration.sql:
--------------------------------------------------------------------------------
1 | /*
2 |   Warnings:
3 | 
4 |   - A unique constraint covering the columns `[id,project_id]` on the table `scores` will be added. If there are existing duplicate values, this will fail.
5 | 
6 | */
7 | -- CreateIndex
8 | CREATE UNIQUE INDEX CONCURRENTLY "scores_id_project_id_key" ON "scores"("id", "project_id");
9 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240522081254_scores_add_author_user_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "scores" ADD COLUMN     "author_user_id" TEXT;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240522095738_scores_add_author_user_id_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "scores_author_user_id_idx" ON "scores"("author_user_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240523142524_scores_add_config_id_idx/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "scores_config_id_idx" ON "scores"("config_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240523142610_scores_add_fk_scores_config_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- AddForeignKey
2 | ALTER TABLE "scores" ADD CONSTRAINT "scores_config_id_fkey" FOREIGN KEY ("config_id") REFERENCES "score_configs"("id") ON DELETE SET NULL ON UPDATE CASCADE;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240524154058_scores_source_enum_add_annotation/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterEnum
2 | ALTER TYPE "ScoreSource" ADD VALUE 'ANNOTATION';
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240524156058_scores_source_backfill_annotation_for_review/migration.sql:
--------------------------------------------------------------------------------
1 | -- Backfill the scores source for 'REVIEW' to be 'ANNOTATION'
2 | UPDATE "scores"
3 | SET "source" = 'ANNOTATION'::"ScoreSource"
4 | WHERE "source" = 'REVIEW'::"ScoreSource";
5 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240524165931_scores_source_enum_drop_review/migration.sql:
--------------------------------------------------------------------------------
 1 | /*
 2 |   Warnings:
 3 | 
 4 |   - The values [REVIEW] on the enum `ScoreSource` will be removed. If these variants are still used in the database, this will fail.
 5 | 
 6 | */
 7 | -- AlterEnum
 8 | BEGIN;
 9 | CREATE TYPE "ScoreSource_new" AS ENUM ('ANNOTATION', 'API', 'EVAL');
10 | ALTER TABLE "scores" ALTER COLUMN "source" TYPE "ScoreSource_new" USING ("source"::text::"ScoreSource_new");
11 | ALTER TYPE "ScoreSource" RENAME TO "ScoreSource_old";
12 | ALTER TYPE "ScoreSource_new" RENAME TO "ScoreSource";
13 | DROP TYPE "ScoreSource_old";
14 | COMMIT;
15 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240524190433_job_executions_add_fk_index_config_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "job_executions_job_configuration_id_idx" ON "job_executions"("job_configuration_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240524190434_job_executions_add_fk_index_score_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "job_executions_job_output_score_id_idx" ON "job_executions"("job_output_score_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240524190435_job_executions_add_fk_index_trace_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "job_executions_job_input_trace_id_idx" ON "job_executions"("job_input_trace_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240524190436_job_executions_index_created_at/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "job_executions_created_at_idx" ON "job_executions"("created_at");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214726_add_cursor_new_columns_observations/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "observations" ADD COLUMN     "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214727_add_cursor_new_columns_scores/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- AlterTable
3 | ALTER TABLE "scores" ADD COLUMN     "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
4 | ADD COLUMN     "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP;
5 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_01/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "audit_logs_updated_at_idx" ON "audit_logs"("updated_at");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_02/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "dataset_items_created_at_idx" ON "dataset_items"("created_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_03/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "dataset_items_updated_at_idx" ON "dataset_items"("updated_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_04/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "dataset_run_items_created_at_idx" ON "dataset_run_items"("created_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_05/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "dataset_run_items_updated_at_idx" ON "dataset_run_items"("updated_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_06/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "dataset_runs_created_at_idx" ON "dataset_runs"("created_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_07/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "dataset_runs_updated_at_idx" ON "dataset_runs"("updated_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_08/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "datasets_created_at_idx" ON "datasets"("created_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_09/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "datasets_updated_at_idx" ON "datasets"("updated_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_10/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "job_executions_updated_at_idx" ON "job_executions"("updated_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_11/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "observations_updated_at_idx" ON "observations"("updated_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_12/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "prompts_created_at_idx" ON "prompts"("created_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_13/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "prompts_updated_at_idx" ON "prompts"("updated_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_14/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "score_configs_created_at_idx" ON "score_configs"("created_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_15/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "score_configs_updated_at_idx" ON "score_configs"("updated_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_16/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "scores_created_at_idx" ON "scores"("created_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_17/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "scores_updated_at_idx" ON "scores"("updated_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_18/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "trace_sessions_updated_at_idx" ON "trace_sessions"("updated_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240603212024_dataset_items_add_index_source_trace_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "dataset_items_source_trace_id_idx" ON "dataset_items" USING HASH ("source_trace_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240604133338_scores_add_index_name/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX "scores_project_id_name_idx" ON "scores"("project_id", "name");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240604133339_score_data_type_add_boolean/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterEnum
2 | ALTER TYPE "ScoreDataType" ADD VALUE 'BOOLEAN';
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240606093356_drop_unused_pricings_table/migration.sql:
--------------------------------------------------------------------------------
 1 | /*
 2 |   Warnings:
 3 | 
 4 |   - You are about to drop the `pricings` table. If the table is not empty, all the data it contains will be lost.
 5 | 
 6 | */
 7 | -- DropTable
 8 | DROP TABLE "pricings";
 9 | 
10 | -- DropEnum
11 | DROP TYPE "PricingUnit";
12 | 
13 | -- DropEnum
14 | DROP TYPE "TokenType";
15 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240606133011_remove_trace_fkey_datasetrunitems/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropForeignKey
2 | ALTER TABLE "dataset_run_items" DROP CONSTRAINT "dataset_run_items_trace_id_fkey";
3 | ALTER TABLE "dataset_run_items" DROP CONSTRAINT "dataset_run_items_observation_id_fkey";
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240607212419_model_price_anthropic_via_google_vertex/migration.sql:
--------------------------------------------------------------------------------
1 | -- Google Vertex uses @ to separate model name and version
2 | 
3 | UPDATE "models" SET "match_pattern" = '(?i)^(claude-3-haiku(-|@)?20240307)
#39; WHERE "id" = 'cltr0w45b000008k1407o9qv1';
4 | 
5 | UPDATE "models" SET "match_pattern" = '(?i)^(claude-3-opus(-|@)?20240229)
#39; WHERE "id" = 'cltgy0iuw000008le3vod1hhy';
6 | 
7 | UPDATE "models" SET "match_pattern" = '(?i)^(claude-3-sonnet(-|@)?20240229)
#39; WHERE "id" = 'cltgy0pp6000108le56se7bl3';


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240612101858_add_index_observations_project_id_prompt_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "observations_project_id_prompt_id_idx" ON "observations"("project_id", "prompt_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240617094803_observations_remove_prompt_fk_constraint/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropForeignKey
2 | ALTER TABLE "observations" DROP CONSTRAINT "observations_prompt_id_fkey";
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240618164950_drop_observations_parent_observation_id_idx/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | DROP INDEX CONCURRENTLY IF EXISTS "observations_parent_observation_id_idx";
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240618164951_drop_observations_updated_at_idx/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | DROP INDEX CONCURRENTLY IF EXISTS "observations_updated_at_idx";
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240618164952_drop_scores_updated_at_idx/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | DROP INDEX CONCURRENTLY IF EXISTS "scores_updated_at_idx";
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240618164953_drop_traces_external_id_idx/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | DROP INDEX CONCURRENTLY IF EXISTS "traces_external_id_idx";
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240618164954_drop_traces_release_idx/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | DROP INDEX CONCURRENTLY IF EXISTS "traces_release_idx";
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240618164955_drop_traces_updated_at_idx/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | DROP INDEX CONCURRENTLY IF EXISTS "traces_updated_at_idx";
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240618164956_create_traces_project_id_timestamp_idx/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "traces_project_id_timestamp_idx" ON "traces"("project_id", "timestamp");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240624133412_models_add_anthropic_3_5_sonnet/migration.sql:
--------------------------------------------------------------------------------
 1 | INSERT INTO models (
 2 |   id,
 3 |   project_id,
 4 |   model_name,
 5 |   match_pattern,
 6 |   start_date,
 7 |   input_price,
 8 |   output_price,
 9 |   total_price,
10 |   unit,
11 |   tokenizer_id
12 | )
13 | VALUES
14 |   -- add 3.5 sonnet model
15 |   ('clxt0n0m60000pumz1j5b7zsf', NULL, 'claude-3-5-sonnet-20240620', '(?i)^(claude-3-5-sonnet(-|@)?20240620)
#39;, NULL, 0.000003, 0.000015, NULL, 'TOKENS', 'claude')


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240625103957_observations_add_calculated_cost_columns/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "observations" ADD COLUMN     "calculated_input_cost" DECIMAL(65,30),
3 | ADD COLUMN     "calculated_output_cost" DECIMAL(65,30),
4 | ADD COLUMN     "calculated_total_cost" DECIMAL(65,30),
5 | ADD COLUMN     "internal_model_id" TEXT;
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240625103958_fix_model_match_gpt4_vision/migration.sql:
--------------------------------------------------------------------------------
 1 | /*
 2 | Previously, the pattern did not allow for model specifications like "1106" or any other 4-digit block. 
 3 | This led to missing models on the generation-update call where the exact model name that was used was provided (including the 4-digit block).
 4 | The new pattern allows for:
 5 | 
 6 | - "gpt-4-vision-preview" as set on generation-create
 7 | - "gpt-4-1106-vision-preview" as set on generation-update
 8 | 
 9 | */
10 | 
11 | UPDATE
12 | 	"models"
13 | SET
14 | 	"match_pattern" = '(?i)^(gpt-4(-\d{4})?-vision-preview)
#39;
15 | WHERE
16 | 	"id" = 'clrkvx5gp000108juaogs54ea'
17 | 	AND "model_name" = 'gpt-4-turbo-vision';


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240704103901_scores_make_value_optional/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "scores" ALTER COLUMN "value" DROP NOT NULL;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240710114043_score_configs_drop_empty_categories_array_for_numeric_scores/migration.sql:
--------------------------------------------------------------------------------
1 | -- Migration script to update score_configs entries
2 | -- Set categories to NULL where data_type is 'NUMERIC' and categories is an empty array
3 | 
4 | UPDATE score_configs
5 | SET categories = NULL
6 | WHERE data_type = 'NUMERIC' AND categories IS NOT NULL;
7 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240718011733_dataset_runs_add_unique_dataset_id_project_id_name copy/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE UNIQUE INDEX CONCURRENTLY "dataset_runs_dataset_id_project_id_name_key" ON "dataset_runs"("dataset_id", "project_id", "name");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240718011734_dataset_runs_drop_unique_dataset_id_name/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | DROP INDEX CONCURRENTLY "dataset_runs_dataset_id_name_key";


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240807111358_models_add_openai_gpt_4o_2024_08_06/migration.sql:
--------------------------------------------------------------------------------
 1 | 
 2 | INSERT INTO models (
 3 |   id,
 4 |   project_id,
 5 |   model_name,
 6 |   match_pattern,
 7 |   start_date,
 8 |   input_price,
 9 |   output_price,
10 |   total_price,
11 |   unit,
12 |   tokenizer_id,
13 |   tokenizer_config
14 | )
15 | VALUES
16 |   -- gpt-4o-2024-08-06
17 |   ('clzjr85f70000ymmzg7hqffra', NULL, 'gpt-4o-2024-08-06', '(?i)^(gpt-4o-2024-08-06)
#39;, NULL, 0.0000025, 0.000010, NULL, 'TOKENS', 'openai', '{ "tokensPerMessage": 3, "tokensPerName": 1, "tokenizerModel": "gpt-4o" }')
18 |   


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240814223824_model_fix_text_embedding_3_large/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- Fix model name
3 | -- https://github.com/langfuse/langfuse/issues/2688
4 | 
5 | UPDATE models
6 | SET model_name = 'text-embedding-3-large'
7 | WHERE id = 'clruwn76700020al7gp8e4g4l'


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240814233029_dataset_items_drop_fkey_on_traces_and_observations/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropForeignKey
2 | ALTER TABLE "dataset_items" DROP CONSTRAINT "dataset_items_source_observation_id_fkey";
3 | 
4 | -- DropForeignKey
5 | ALTER TABLE "dataset_items" DROP CONSTRAINT "dataset_items_source_trace_id_fkey";
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240913185822_account_add_refresh_token_expires_in/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "Account" ADD COLUMN     "refresh_token_expires_in" INTEGER;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183001_remove_covered_indexes_01/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "traces_project_id_idx"; -- covered by traces_project_id_timestamp_idx
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183002_remove_covered_indexes_02/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "datasets_project_id_idx"; -- covered by datasets_project_id_name_key (unique)
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183003_remove_covered_indexes_03/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "eval_templates_project_id_idx"; -- covered by eval_templates_project_id_id_idx
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183004_remove_covered_indexes_04/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "job_configurations_project_id_idx"; -- covered by job_configurations_project_id_id_idx
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183005_remove_covered_indexes_05/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "job_executions_project_id_idx"; -- covered by job_executions_project_id_id_idx
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183006_remove_covered_indexes_06/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "llm_api_keys_project_id_provider_idx"; -- covered by llm_api_keys_project_id_provider_key (unique)
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183007_remove_covered_indexes_07/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "models_project_id_model_name_idx"; -- covered by models_project_id_model_name_start_date_unit_key (unique)
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183008_remove_covered_indexes_08/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "models_project_id_model_name_start_date_unit_idx"; -- covered by models_project_id_model_name_start_date_unit_key (unique)
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183009_remove_covered_indexes_09/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "observations_project_id_idx"; -- covered by observations_project_id_start_time_type_idx
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183010_remove_covered_indexes_10/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "observations_trace_id_idx"; -- covered by observations_trace_id_project_id_start_time_idx
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183011_remove_covered_indexes_11/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "observations_trace_id_project_id_idx"; -- covered by observations_trace_id_project_id_start_time_idx
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183012_remove_covered_indexes_12/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "organization_memberships_org_id_idx"; -- covered by organization_memberships_org_id_user_id_key (unique)
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183013_remove_covered_indexes_13/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "posthog_integrations_project_id_idx"; -- covered by posthog_integrations_pkey (unique)
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183014_remove_covered_indexes_14/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "prompts_project_id_idx"; -- covered by prompts_project_id_name_version_key (unique)
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183015_remove_covered_indexes_15/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "prompts_project_id_name_version_idx"; -- covered by prompts_project_id_name_version_key (unique)
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183016_remove_covered_indexes_16/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "scores_project_id_idx"; -- covered by scores_project_id_name_idx
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20241009042557_auth_add_created_at_for_gitlab/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "Account" ADD COLUMN     "created_at" INTEGER;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20241009110720_scores_add_nullable_queue_id_column/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "scores" ADD COLUMN     "queue_id" TEXT;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20241010120245_llm_keys_add_config/migration.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE "llm_api_keys" ADD COLUMN "config" JSONB;


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20241023110145_update_claude_sonnet_35/migration.sql:
--------------------------------------------------------------------------------
1 | -- https://docs.anthropic.com/en/docs/about-claude/models#model-comparison-table
2 | UPDATE models SET model_name = 'claude-3.5-sonnet-20241022' WHERE id = 'cm2krz1uf000208jjg5653iud';
3 | UPDATE models SET model_name = 'claude-3.5-sonnet-latest' WHERE id = 'cm2ks2vzn000308jjh4ze1w7q';


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20241024111800_add_background_migrations_table/migration.sql:
--------------------------------------------------------------------------------
 1 | -- CreateTable
 2 | CREATE TABLE "background_migrations" (
 3 |     "id" TEXT NOT NULL,
 4 |     "name" TEXT NOT NULL,
 5 |     "script" TEXT NOT NULL,
 6 |     "args" JSONB NOT NULL,
 7 | 
 8 |     "finished_at" TIMESTAMP(3),
 9 |     "failed_at" TIMESTAMP(3),
10 |     "failed_reason" TEXT,
11 |     "worker_id" TEXT,
12 |     "locked_at" TIMESTAMP(3),
13 | 
14 |     CONSTRAINT "background_migrations_pkey" PRIMARY KEY ("id")
15 | );
16 | 
17 | -- CreateIndex
18 | CREATE UNIQUE INDEX "background_migrations_name_key" ON "background_migrations"("name");
19 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20241024121500_add_generations_cost_backfill_background_migration/migration.sql:
--------------------------------------------------------------------------------
1 | INSERT INTO background_migrations (id, name, script, args)
2 | VALUES ('32859a35-98f5-4a4a-b438-ebc579349e00', '20241024_1216_add_generations_cost_backfill', 'addGenerationsCostBackfill', '{}');
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20241024173000_add_traces_pg_to_ch_background_migration/migration.sql:
--------------------------------------------------------------------------------
1 | INSERT INTO background_migrations (id, name, script, args)
2 | VALUES ('5960f22a-748f-480c-b2f3-bc4f9d5d84bc', '20241024_1730_migrate_traces_from_pg_to_ch', 'migrateTracesFromPostgresToClickhouse', '{}');
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20241024173700_add_observations_pg_to_ch_background_migration/migration.sql:
--------------------------------------------------------------------------------
1 | INSERT INTO background_migrations (id, name, script, args)
2 | VALUES ('7526e7c9-0026-4595-af2c-369dfd9176ec', '20241024_1737_migrate_observations_from_pg_to_ch', 'migrateObservationsFromPostgresToClickhouse', '{}');
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20241024173800_add_scores_pg_to_ch_background_migration/migration.sql:
--------------------------------------------------------------------------------
1 | INSERT INTO background_migrations (id, name, script, args)
2 | VALUES ('94e50334-50d3-4e49-ad2e-9f6d92c85ef7', '20241024_1738_migrate_scores_from_pg_to_ch', 'migrateScoresFromPostgresToClickhouse', '{}');
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20241029130802_prices_drop_excess_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | DROP INDEX CONCURRENTLY "prices_model_id_idx";
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20241104111600_background_migrations_add_state_column/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "background_migrations" ADD COLUMN "state" jsonb NOT NULL DEFAULT '{}';


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20241114175010_job_executions_add_observation_dataset_item_cols/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropForeignKey
2 | ALTER TABLE "job_executions" DROP CONSTRAINT "job_executions_job_input_trace_id_fkey";
3 | 
4 | -- AlterTable
5 | ALTER TABLE "job_executions" ADD COLUMN     "job_input_dataset_item_id" TEXT,
6 | ADD COLUMN     "job_input_observation_id" TEXT;
7 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20241124115100_add_projects_deleted_at/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "projects" ADD COLUMN "deleted_at" TIMESTAMP(3);
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20241206115829_remove_trace_score_observation_constraints/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropForeignKey
2 | ALTER TABLE "job_executions" DROP CONSTRAINT "job_executions_job_output_score_id_fkey";
3 | 
4 | -- DropForeignKey
5 | ALTER TABLE "traces" DROP CONSTRAINT "traces_session_id_project_id_fkey";
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250108220721_add_queue_backup_table/migration.sql:
--------------------------------------------------------------------------------
 1 | -- CreateTable
 2 | CREATE TABLE "queue_backups" (
 3 |     "id" TEXT NOT NULL,
 4 |     "project_id" TEXT,
 5 |     "queue_name" TEXT NOT NULL,
 6 |     "content" JSONB NOT NULL,
 7 |     "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
 8 | 
 9 |     CONSTRAINT "queue_backups_pkey" PRIMARY KEY ("id")
10 | );
11 | 
12 | -- AddForeignKey
13 | ALTER TABLE "traces" ADD CONSTRAINT "traces_session_id_project_id_fkey" FOREIGN KEY ("session_id", "project_id") REFERENCES "trace_sessions"("id", "project_id") ON DELETE RESTRICT ON UPDATE CASCADE;
14 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250109083346_drop_trace_tracesession_fk/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropForeignKey
2 | ALTER TABLE "traces" DROP CONSTRAINT "traces_session_id_project_id_fkey";
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250122152102_add_llm_api_keys_extra_headers/migration.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE "llm_api_keys"
2 |     ADD COLUMN "extra_headers" TEXT,
3 |     ADD COLUMN "extra_header_keys" TEXT[] NOT NULL DEFAULT '{}'::TEXT[];
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250123103200_add_retention_days_to_projects/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "projects"
3 |     ADD COLUMN "retention_days" INTEGER;
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250128144418_llm_adapter_rename_google_vertex_ai/migration.sql:
--------------------------------------------------------------------------------
1 | UPDATE "llm_api_keys" SET adapter = 'google-vertex-ai' WHERE adapter = 'vertex-ai';
2 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250128163035_add_nullable_commit_message_prompts/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "prompts" ADD COLUMN     "commit_message" TEXT;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250211102600_drop_event_log_table/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropTable
2 | DROP TABLE event_log;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250211123300_drop_events_table/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropTable
2 | DROP TABLE events;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250214173309_add_timescope_to_configs/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "job_configurations" ADD COLUMN     "time_scope" TEXT[] DEFAULT ARRAY['NEW']::TEXT[];
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250220141500_add_environment_to_trace_sessions/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "trace_sessions"
3 | ADD COLUMN "environment" TEXT NOT NULL DEFAULT 'default';
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250221143400_drop_trace_view_observation_view/migration.sql:
--------------------------------------------------------------------------------
1 | DROP VIEW IF EXISTS "observations_view";
2 | DROP VIEW IF EXISTS "traces_view";


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250310100328_add_api_key_to_audit_log/migration.sql:
--------------------------------------------------------------------------------
 1 | -- CreateEnum
 2 | CREATE TYPE "AuditLogRecordType" AS ENUM ('USER', 'API_KEY');
 3 | 
 4 | -- AlterTable
 5 | ALTER TABLE "audit_logs" ADD COLUMN     "api_key_id" TEXT,
 6 | ADD COLUMN     "type" "AuditLogRecordType" NOT NULL DEFAULT 'USER',
 7 | ALTER COLUMN "user_id" DROP NOT NULL,
 8 | ALTER COLUMN "user_org_role" DROP NOT NULL;
 9 | 
10 | -- CreateIndex
11 | CREATE INDEX "audit_logs_api_key_id_idx" ON "audit_logs"("api_key_id");
12 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250321102240_drop_queue_backup_table/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropTable
2 | DROP TABLE "queue_backups";
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250402142320_add_blobstorage_integration_file_type/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateEnum
2 | CREATE TYPE "BlobStorageIntegrationFileType" AS ENUM ('JSON', 'CSV', 'JSONL');
3 | 
4 | -- AlterTable
5 | ALTER TABLE "blob_storage_integrations" ADD COLUMN     "file_type" "BlobStorageIntegrationFileType" NOT NULL DEFAULT 'CSV';
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250403153555_membership_invitations_no_duplicates/migration.sql:
--------------------------------------------------------------------------------
 1 | -- Delete duplicate membership invitations, keeping only the newest one for each email and org_id combination
 2 | WITH ranked_invitations AS (
 3 |   SELECT 
 4 |     id,
 5 |     email,
 6 |     org_id,
 7 |     ROW_NUMBER() OVER (PARTITION BY email, org_id ORDER BY updated_at DESC) as rn
 8 |   FROM membership_invitations
 9 | )
10 | DELETE FROM membership_invitations
11 | WHERE id IN (
12 |   SELECT id FROM ranked_invitations WHERE rn > 1
13 | );
14 | 
15 | 
16 | -- CreateIndex
17 | CREATE UNIQUE INDEX "membership_invitations_email_org_id_key" ON "membership_invitations"("email", "org_id");
18 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250410145712_add_organization_scoped_api_keys/migration.sql:
--------------------------------------------------------------------------------
 1 | -- CreateEnum
 2 | CREATE TYPE "ApiKeyScope" AS ENUM ('ORGANIZATION', 'PROJECT');
 3 | 
 4 | -- AlterTable
 5 | ALTER TABLE "api_keys" ADD COLUMN     "organization_id" TEXT,
 6 | ADD COLUMN     "scope" "ApiKeyScope" NOT NULL DEFAULT 'PROJECT',
 7 | ALTER COLUMN "project_id" DROP NOT NULL;
 8 | 
 9 | -- CreateIndex
10 | CREATE INDEX "api_keys_organization_id_idx" ON "api_keys"("organization_id");
11 | 
12 | -- AddForeignKey
13 | ALTER TABLE "api_keys" ADD CONSTRAINT "api_keys_organization_id_fkey" FOREIGN KEY ("organization_id") REFERENCES "organizations"("id") ON DELETE CASCADE ON UPDATE CASCADE;
14 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250420120553_add_organization_and_project_metadata/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "organizations" ADD COLUMN     "metadata" JSONB;
3 | 
4 | -- AlterTable
5 | ALTER TABLE "projects" ADD COLUMN     "metadata" JSONB;
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250517173700_add_event_log_migration_background_migration.sql/migration.sql:
--------------------------------------------------------------------------------
1 | INSERT INTO background_migrations (id, name, script, args)
2 | VALUES ('c19b91d9-f9a2-468b-8209-95578f970c5b', '20250417_1737_migrate_event_log_to_blob_storage', 'migrateEventLogToBlobStorageRefTable', '{}');
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250519073249_add_trace_media_media_id_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY IF NOT EXISTS "trace_media_project_id_media_id_idx" ON "trace_media"("project_id", "media_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250519073327_add_observation_media_media_id_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY IF NOT EXISTS "observation_media_project_id_media_id_idx" ON "observation_media"("project_id", "media_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250519093327_media_add_index_project_id_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- Index cannot be created concurrently in a transaction, so we need to create it separately
2 | -- Prerequisite for migration 20250518075613_media_relax_id_uniqueness_to_project_only
3 | CREATE UNIQUE INDEX CONCURRENTLY IF NOT EXISTS "media_project_id_id_key" ON "media"("project_id", "id");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250520123737_add_single_aggregate_chart_type/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterEnum
2 | ALTER TYPE "DashboardWidgetChartType" ADD VALUE 'NUMBER';
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250522140357_remove_obsolete_observation_media_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | DROP INDEX CONCURRENTLY IF EXISTS "observation_media_project_id_observation_id_idx";
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250523110540_modify_nullable_cols_eval_templates/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "eval_templates" ALTER COLUMN "project_id" DROP NOT NULL;
3 | ALTER TABLE "eval_templates" ALTER COLUMN "model" DROP NOT NULL;
4 | ALTER TABLE "eval_templates" ALTER COLUMN "provider" DROP NOT NULL;
5 | ALTER TABLE "eval_templates" ALTER COLUMN "model_params" DROP NOT NULL;
6 | ALTER TABLE "eval_templates" ADD COLUMN "partner" TEXT;


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250523120545_add_nullable_job_template_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "job_executions" ADD COLUMN "job_template_id" TEXT;
3 | ALTER TABLE "job_executions" ADD CONSTRAINT "job_executions_job_template_id_fkey" FOREIGN KEY ("job_template_id") REFERENCES "eval_templates"("id") ON DELETE SET NULL;
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250529071241_make_blobstorage_integration_credentials_optional/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "blob_storage_integrations" ALTER COLUMN "access_key_id" DROP NOT NULL,
3 | ALTER COLUMN "secret_access_key" DROP NOT NULL;
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250604085536_add_histogram_chart_type/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterEnum
2 | ALTER TYPE "DashboardWidgetChartType" ADD VALUE 'HISTOGRAM';
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/migration_lock.toml:
--------------------------------------------------------------------------------
1 | # Please do not edit this file manually
2 | # It should be added in your version-control system (e.g., Git)
3 | provider = "postgresql"


--------------------------------------------------------------------------------
/packages/shared/scripts/cleanup.sql:
--------------------------------------------------------------------------------
1 | DO $
2 | BEGIN
3 |  IF EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = '_prisma_migrations') THEN
4 |   DELETE FROM _prisma_migrations
5 |   WHERE migration_name IN ('20240606090858_pricings_add_latest_gemini_models', '20240530212419_model_price_anthropic_via_google_vertex', '20240604133340_backfill_manual_scores');
6 |  END IF;
7 | END $;


--------------------------------------------------------------------------------
/packages/shared/src/constants.ts:
--------------------------------------------------------------------------------
 1 | /* eslint-disable no-unused-vars */
 2 | // disable lint as this is exported and used in packages
 3 | export enum ModelUsageUnit {
 4 |   Characters = "CHARACTERS",
 5 |   Tokens = "TOKENS",
 6 |   Seconds = "SECONDS",
 7 |   Milliseconds = "MILLISECONDS",
 8 |   Images = "IMAGES",
 9 |   Requests = "REQUESTS",
10 | }
11 | 


--------------------------------------------------------------------------------
/packages/shared/src/domain/index.ts:
--------------------------------------------------------------------------------
1 | export * from "./observations";
2 | export * from "./traces";
3 | export * from "./scores";
4 | export * from "./table-view-presets";
5 | 


--------------------------------------------------------------------------------
/packages/shared/src/errors/ApiError.ts:
--------------------------------------------------------------------------------
1 | import { BaseError } from "./BaseError";
2 | 
3 | export class ApiError extends BaseError {
4 |   constructor(description = "Api call failed", status = 500) {
5 |     super("ApiError", status, description, true);
6 |   }
7 | }
8 | 


--------------------------------------------------------------------------------
/packages/shared/src/errors/BaseError.ts:
--------------------------------------------------------------------------------
 1 | export class BaseError extends Error {
 2 |   public readonly name: string;
 3 |   public readonly httpCode: number;
 4 |   public readonly isOperational: boolean;
 5 | 
 6 |   constructor(
 7 |     name: string,
 8 |     httpCode: number,
 9 |     description: string,
10 |     isOperational: boolean
11 |   ) {
12 |     super(description);
13 |     Object.setPrototypeOf(this, new.target.prototype); // restore prototype chain
14 | 
15 |     this.name = name;
16 |     this.httpCode = httpCode;
17 |     this.isOperational = isOperational; // if error is part of known errors that our application can anticipate
18 | 
19 |     Error.captureStackTrace(this);
20 |   }
21 | }
22 | 


--------------------------------------------------------------------------------
/packages/shared/src/errors/ConflictError.ts:
--------------------------------------------------------------------------------
1 | import { BaseError } from "./BaseError";
2 | 
3 | export class LangfuseConflictError extends BaseError {
4 |   constructor(description = "Conflict") {
5 |     super("LangfuseConflictError", 409, description, true);
6 |   }
7 | }
8 | 


--------------------------------------------------------------------------------
/packages/shared/src/errors/ForbiddenError.ts:
--------------------------------------------------------------------------------
1 | import { BaseError } from "./BaseError";
2 | 
3 | export class ForbiddenError extends BaseError {
4 |   constructor(description = "Forbidden") {
5 |     super("ForbiddenError", 403, description, true);
6 |   }
7 | }
8 | 


--------------------------------------------------------------------------------
/packages/shared/src/errors/InternalServerError.ts:
--------------------------------------------------------------------------------
1 | import { BaseError } from "./BaseError";
2 | 
3 | export class InternalServerError extends BaseError {
4 |   constructor(description = "Internal Server Error") {
5 |     super("InternalServerError", 500, description, true);
6 |   }
7 | }
8 | 


--------------------------------------------------------------------------------
/packages/shared/src/errors/InvalidRequestError.ts:
--------------------------------------------------------------------------------
1 | import { BaseError } from "./BaseError";
2 | 
3 | export class InvalidRequestError extends BaseError {
4 |   constructor(description = "Invalid Request Error") {
5 |     super("InvalidRequestError", 400, description, true);
6 |   }
7 | }
8 | 


--------------------------------------------------------------------------------
/packages/shared/src/errors/MethodNotAllowedError.ts:
--------------------------------------------------------------------------------
1 | import { BaseError } from "./BaseError";
2 | 
3 | export class MethodNotAllowedError extends BaseError {
4 |   constructor(description = "Method not allowed") {
5 |     super("MethodNotAllowedError", 405, description, true);
6 |   }
7 | }
8 | 


--------------------------------------------------------------------------------
/packages/shared/src/errors/NotFoundError.ts:
--------------------------------------------------------------------------------
1 | import { BaseError } from "./BaseError";
2 | 
3 | export class LangfuseNotFoundError extends BaseError {
4 |   constructor(description = "Not Found") {
5 |     super("LangfuseNotFoundError", 404, description, true);
6 |   }
7 | }
8 | 


--------------------------------------------------------------------------------
/packages/shared/src/errors/UnauthorizedError.ts:
--------------------------------------------------------------------------------
1 | import { BaseError } from "./BaseError";
2 | 
3 | export class UnauthorizedError extends BaseError {
4 |   constructor(description = "Unauthorized") {
5 |     super("UnauthorizedError", 401, description, true);
6 |   }
7 | }
8 | 


--------------------------------------------------------------------------------
/packages/shared/src/errors/index.ts:
--------------------------------------------------------------------------------
 1 | export { BaseError } from "./BaseError";
 2 | export { LangfuseNotFoundError } from "./NotFoundError";
 3 | export { InvalidRequestError } from "./InvalidRequestError";
 4 | export { UnauthorizedError } from "./UnauthorizedError";
 5 | export { ForbiddenError } from "./ForbiddenError";
 6 | export { MethodNotAllowedError } from "./MethodNotAllowedError";
 7 | export { ApiError } from "./ApiError";
 8 | export { InternalServerError } from "./InternalServerError";
 9 | export { LangfuseConflictError } from "./ConflictError";
10 | 


--------------------------------------------------------------------------------
/packages/shared/src/features/comments/types.ts:
--------------------------------------------------------------------------------
 1 | import { z } from "zod/v4";
 2 | 
 3 | const MAX_COMMENT_LENGTH = 3000;
 4 | 
 5 | const COMMENT_OBJECT_TYPES = [
 6 |   "TRACE",
 7 |   "OBSERVATION",
 8 |   "SESSION",
 9 |   "PROMPT",
10 | ] as const;
11 | 
12 | export const CreateCommentData = z.object({
13 |   projectId: z.string(),
14 |   content: z.string().trim().min(1).max(MAX_COMMENT_LENGTH),
15 |   objectId: z.string(),
16 |   objectType: z.enum(COMMENT_OBJECT_TYPES),
17 | });
18 | 
19 | export const DeleteCommentData = z.object({
20 |   projectId: z.string(),
21 |   commentId: z.string(),
22 |   objectId: z.string(),
23 |   objectType: z.enum(COMMENT_OBJECT_TYPES),
24 | });
25 | 


--------------------------------------------------------------------------------
/packages/shared/src/features/experiments/utils.ts:
--------------------------------------------------------------------------------
 1 | import { Prisma } from "../../db";
 2 | 
 3 | export const datasetItemMatchesVariable = (
 4 |   input: Prisma.JsonValue,
 5 |   variable: string,
 6 | ) => {
 7 |   if (
 8 |     input === null ||
 9 |     input === undefined ||
10 |     typeof input !== "object" ||
11 |     Array.isArray(input)
12 |   )
13 |     return false;
14 |   return Object.keys(input).includes(variable);
15 | };
16 | 


--------------------------------------------------------------------------------
/packages/shared/src/features/scores/index.ts:
--------------------------------------------------------------------------------
1 | export * from "./interfaces";
2 | export * from "./scoreConfigTypes";
3 | 


--------------------------------------------------------------------------------
/packages/shared/src/features/scores/interfaces/api/index.ts:
--------------------------------------------------------------------------------
1 | export * from "./v1/schemas";
2 | export * from "./v1/validation";
3 | export * from "./v1/endpoints";
4 | export * from "./v2/schemas";
5 | export * from "./v2/validation";
6 | export * from "./v2/endpoints";
7 | 


--------------------------------------------------------------------------------
/packages/shared/src/features/scores/interfaces/index.ts:
--------------------------------------------------------------------------------
1 | export * from "./api";
2 | export * from "./application/validation";
3 | export * from "./ingestion/validation";
4 | export * from "./ui/types";
5 | 


--------------------------------------------------------------------------------
/packages/shared/src/interfaces/orderBy.ts:
--------------------------------------------------------------------------------
 1 | import { z } from "zod/v4";
 2 | 
 3 | export const orderBy = z
 4 |   .object({
 5 |     column: z.string(),
 6 |     order: z.enum(["ASC", "DESC"]),
 7 |   })
 8 |   .nullable();
 9 | 
10 | export type OrderByState = z.infer<typeof orderBy>;
11 | 


--------------------------------------------------------------------------------
/packages/shared/src/interfaces/parseDbOrg.ts:
--------------------------------------------------------------------------------
 1 | import { type Organization } from "@prisma/client";
 2 | import { CloudConfigSchema } from "./cloudConfigSchema";
 3 | 
 4 | type parsedOrg = Omit<Organization, "cloudConfig"> & {
 5 |   cloudConfig: CloudConfigSchema | null;
 6 | };
 7 | 
 8 | export function parseDbOrg(dbOrg: Organization): parsedOrg {
 9 |   const { cloudConfig, ...org } = dbOrg;
10 | 
11 |   const parsedCloudConfig = CloudConfigSchema.safeParse(cloudConfig);
12 | 
13 |   const parsedOrg = {
14 |     ...org,
15 |     cloudConfig: parsedCloudConfig.success ? parsedCloudConfig.data : null,
16 |   };
17 | 
18 |   return parsedOrg;
19 | }
20 | 


--------------------------------------------------------------------------------
/packages/shared/src/interfaces/search.ts:
--------------------------------------------------------------------------------
1 | import { z } from "zod/v4";
2 | 
3 | export const TracingSearchType = z.enum(["id", "content"]);
4 | // id: for searching smaller columns like IDs, types, and other metadata
5 | // content: for searching input/output text of functions traced via OpenTelemetry
6 | export type TracingSearchType = z.infer<typeof TracingSearchType>;
7 | 


--------------------------------------------------------------------------------
/packages/shared/src/interfaces/tableNames.ts:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Shared table names used across batch operations (exports, actions, etc.)
 3 |  * This enum provides a centralized definition of database table names
 4 |  * to avoid coupling between different batch operation types.
 5 |  */
 6 | export enum BatchTableNames {
 7 |   Scores = "scores",
 8 |   Sessions = "sessions",
 9 |   Traces = "traces",
10 |   Observations = "observations",
11 |   DatasetRunItems = "dataset_run_items",
12 |   AuditLogs = "audit_logs",
13 | }
14 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/clickhouse/schema.ts:
--------------------------------------------------------------------------------
 1 | export const ClickhouseTableNames = {
 2 |   traces: "traces",
 3 |   observations: "observations",
 4 |   scores: "scores",
 5 | 
 6 |   // Virtual tables for dashboards
 7 |   // TODO: Check if we can do this more elegantly
 8 |   scores_numeric: "scores_numeric",
 9 |   scores_categorical: "scores_categorical",
10 | } as const;
11 | 
12 | export type ClickhouseTableName = keyof typeof ClickhouseTableNames;
13 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/llm/utils.ts:
--------------------------------------------------------------------------------
 1 | import { z } from "zod/v4";
 2 | 
 3 | import { decrypt } from "../../encryption";
 4 | 
 5 | const ExtraHeaderSchema = z.record(z.string(), z.string());
 6 | 
 7 | export function decryptAndParseExtraHeaders(
 8 |   extraHeaders: string | null | undefined,
 9 | ) {
10 |   if (!extraHeaders) return;
11 | 
12 |   return ExtraHeaderSchema.parse(JSON.parse(decrypt(extraHeaders)));
13 | }
14 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/queries/createGenerationsQuery.ts:
--------------------------------------------------------------------------------
 1 | import { Observation } from "../../domain";
 2 | 
 3 | type AdditionalObservationFields = {
 4 |   traceName: string | null;
 5 |   traceTags: Array<string>;
 6 |   traceTimestamp: Date | null;
 7 | };
 8 | 
 9 | export type FullObservation = AdditionalObservationFields & Observation;
10 | 
11 | export type FullObservations = Array<FullObservation>;
12 | 
13 | export type FullObservationsWithScores = Array<
14 |   FullObservation & { scores?: Record<string, string[] | number[]> | null }
15 | >;
16 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/queries/types.ts:
--------------------------------------------------------------------------------
 1 | import z from "zod/v4";
 2 | import { singleFilter } from "../../interfaces/filters";
 3 | import { orderBy } from "../../interfaces/orderBy";
 4 | import { optionalPaginationZod } from "../../utils/zod";
 5 | 
 6 | const TableFilterSchema = z.object({
 7 |   projectId: z.string(),
 8 |   filter: z.array(singleFilter).nullish(),
 9 |   searchQuery: z.string().nullish(),
10 |   orderBy: orderBy,
11 |   ...optionalPaginationZod,
12 | });
13 | 
14 | export type TableFilters = z.infer<typeof TableFilterSchema>;
15 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/repositories/constants.ts:
--------------------------------------------------------------------------------
 1 | // Rule of thumb: If you join observations from left, use observations to trace and vice versa
 2 | 
 3 | // t.timestamp > observation.start_time - 2 days
 4 | export const OBSERVATIONS_TO_TRACE_INTERVAL = "INTERVAL 2 DAY";
 5 | // observation.start_time > t.timestamp - 1 hour
 6 | export const TRACE_TO_OBSERVATIONS_INTERVAL = "INTERVAL 1 HOUR";
 7 | // observation.start_time > s.timestamp - 1 hour
 8 | // t.timestamp > s.timestamp - 1 hour
 9 | export const SCORE_TO_TRACE_OBSERVATIONS_INTERVAL = "INTERVAL 1 HOUR";
10 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/repositories/index.ts:
--------------------------------------------------------------------------------
 1 | export * from "./scores";
 2 | export * from "./traces";
 3 | export * from "./observations";
 4 | export * from "./types";
 5 | export * from "./dashboards";
 6 | export * from "./traces_converters";
 7 | export * from "./scores_converters";
 8 | export * from "./observations_converters";
 9 | export * from "./clickhouse";
10 | export * from "./constants";
11 | export * from "./trace-sessions";
12 | export * from "./scores-utils";
13 | export * from "./blobStorageLog";
14 | export * from "./environments";
15 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/repositories/types.ts:
--------------------------------------------------------------------------------
1 | export type TableCount = {
2 |   count: number;
3 | };
4 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/services/DashboardService/index.ts:
--------------------------------------------------------------------------------
1 | export * from "./DashboardService";
2 | export * from "./types";
3 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/services/DefaultEvaluationModelService/index.ts:
--------------------------------------------------------------------------------
1 | export * from "./DefaultEvalModelService";
2 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/services/PromptService/utils.ts:
--------------------------------------------------------------------------------
1 | export function escapeRegex(str: string | number) {
2 |   return String(str).replace(/[.*+?^${}()|[\]\\]/g, "\\
amp;");
3 | }
4 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/services/TableViewService/index.ts:
--------------------------------------------------------------------------------
1 | export * from "./TableViewService";
2 | export * from "./types";
3 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/test-utils/index.ts:
--------------------------------------------------------------------------------
1 | export * from "./tracing-factory";
2 | export * from "./clickhouse-helpers";
3 | export * from "./org-factory";
4 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/utils/metadata_conversion.ts:
--------------------------------------------------------------------------------
 1 | import { parseJsonPrioritised } from "../../utils/json";
 2 | import { MetadataDomain } from "../../domain";
 3 | 
 4 | export function parseMetadataCHRecordToDomain(
 5 |   metadata: Record<string, string>,
 6 | ): MetadataDomain {
 7 |   return metadata
 8 |     ? Object.fromEntries(
 9 |         Object.entries(metadata ?? {}).map(([key, val]) => [
10 |           key,
11 |           val === null ? null : parseJsonPrioritised(val),
12 |         ]),
13 |       )
14 |     : {};
15 | }
16 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/utils/transforms/index.ts:
--------------------------------------------------------------------------------
 1 | import { Transform } from "stream";
 2 | 
 3 | import { BatchExportFileFormat } from "../../../features/batchExport/types";
 4 | import { transformStreamToCsv } from "./transformStreamToCsv";
 5 | import { transformStreamToJson } from "./transformStreamToJson";
 6 | import { transformStreamToJsonl } from "./transformStreamToJsonl";
 7 | 
 8 | export const streamTransformations: Record<
 9 |   BatchExportFileFormat,
10 |   () => Transform
11 | > = {
12 |   CSV: transformStreamToCsv,
13 |   JSON: transformStreamToJson,
14 |   JSONL: transformStreamToJsonl,
15 | };
16 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/utils/transforms/stringify.ts:
--------------------------------------------------------------------------------
1 | export const stringify = (data: any): string => {
2 |   return JSON.stringify(data, (key, value) =>
3 |     typeof value === "bigint" ? Number.parseInt(value.toString()) : value
4 |   );
5 | };
6 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/utils/transforms/transformStreamToJsonl.ts:
--------------------------------------------------------------------------------
 1 | import { Transform, type TransformCallback } from "stream";
 2 | import { stringify } from "./stringify";
 3 | 
 4 | export function transformStreamToJsonl(): Transform {
 5 |   return new Transform({
 6 |     objectMode: true,
 7 | 
 8 |     transform(
 9 |       row: Record<string, any>,
10 |       encoding: BufferEncoding,
11 |       callback: TransformCallback,
12 |     ): void {
13 |       this.push(stringify(row) + "\n");
14 |       callback();
15 |     },
16 |   });
17 | }
18 | 


--------------------------------------------------------------------------------
/packages/shared/src/tableDefinitions/index.ts:
--------------------------------------------------------------------------------
1 | export * from "./sessionsView";
2 | export * from "./types";
3 | export * from "./mapObservationsTable";
4 | export * from "./mapTracesTable";
5 | export * from "./mapDashboards";
6 | export * from "./mapScoresTable";
7 | 


--------------------------------------------------------------------------------
/packages/shared/src/utils/environment.ts:
--------------------------------------------------------------------------------
 1 | // https://github.com/t3-oss/t3-env/blob/e7e21095e00a477e37608783defda5a6a99586d0/packages/core/src/index.ts#L228
 2 | // unfortunately, we are not able to install t3-env in all our packaging as some rely on commonjs.
 3 | export const removeEmptyEnvVariables = (runtimeEnv: any) => {
 4 |   for (const [key, value] of Object.entries(runtimeEnv)) {
 5 |     if (value === "") {
 6 |       delete runtimeEnv[key];
 7 |     }
 8 |   }
 9 |   return runtimeEnv;
10 | };
11 | 


--------------------------------------------------------------------------------
/packages/shared/src/utils/objects.ts:
--------------------------------------------------------------------------------
 1 | type OmitKeys<T, K extends keyof T> = Pick<T, Exclude<keyof T, K>>;
 2 | 
 3 | /**
 4 |  * Removes specified keys from an object and returns a new object without those keys.
 5 |  */
 6 | 
 7 | export function removeObjectKeys<T, K extends keyof T>(
 8 |   obj: T,
 9 |   keys: K[]
10 | ): OmitKeys<T, K> {
11 |   const result = { ...obj };
12 |   for (const key of keys) {
13 |     delete result[key];
14 |   }
15 |   return result;
16 | }
17 | 


--------------------------------------------------------------------------------
/packages/shared/src/utils/typeChecks.ts:
--------------------------------------------------------------------------------
1 | import { z } from "zod/v4";
2 | 
3 | export const isPresent = <T>(value: T | null | undefined): value is T =>
4 |   value !== null && value !== undefined && value !== "";
5 | 
6 | export const stringDateTime = z.string().datetime({ offset: true }).nullish();
7 | 


--------------------------------------------------------------------------------
/packages/shared/tsconfig.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "extends": "@repo/typescript-config/base.json",
 3 |   "compilerOptions": {
 4 |     "jsx": "react",
 5 |     "moduleResolution": "NodeNext",
 6 |     "module": "NodeNext",
 7 |     "lib": ["ES2021"],
 8 |     "outDir": "./dist",
 9 |     "types": ["node"],
10 |     "target": "ES2020",
11 |     "rootDir": "."
12 |   },
13 |   "include": ["."],
14 |   "exclude": ["node_modules", "dist"]
15 | }
16 | 


--------------------------------------------------------------------------------
/pnpm-workspace.yaml:
--------------------------------------------------------------------------------
1 | packages:
2 |   # include packages in subfolders (e.g. apps/ and packages/)
3 |   - "web"
4 |   - "worker"
5 |   - "packages/**"
6 |   - "ee"
7 | 


--------------------------------------------------------------------------------
/scripts/nuke.sh:
--------------------------------------------------------------------------------
 1 | 
 2 | #  used to nuke the dev environment for engineers
 3 | 
 4 | find . -name 'node_modules' -type d -prune -print -exec rm -rf '{}' \;
 5 | find . -name '.next' -type d -prune -print -exec rm -rf '{}' \;
 6 | find . -iname "bin" -type d -prune -print -exec rm -rf '{}' \;
 7 | find . -iname "dist" -type d -prune -print -exec rm -rf '{}' \;
 8 | find . -iname "out" -type d -prune -print -exec rm -rf '{}' \;
 9 | find . -iname ".turbo" -type d -prune -print -exec rm -rf '{}' \;
10 | find . -iname "tsconfig.tsbuildinfo" -type d -prune -print -exec rm -rf '{}' \;
11 | 
12 | pnpm store prune
13 | 


--------------------------------------------------------------------------------
/web/.eslintrc.js:
--------------------------------------------------------------------------------
1 | /** @type {import("eslint").Linter.Config} */
2 | module.exports = {
3 |   extends: ["@repo/eslint-config/next.js"],
4 |   parser: "@typescript-eslint/parser",
5 |   parserOptions: {
6 |     project: true,
7 |   },
8 | };
9 | 


--------------------------------------------------------------------------------
/web/components.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "$schema": "https://ui.shadcn.com/schema.json",
 3 |   "style": "default",
 4 |   "rsc": true,
 5 |   "tailwind": {
 6 |     "config": "tailwind.config.ts",
 7 |     "css": "src/styles/globals.css",
 8 |     "baseColor": "slate",
 9 |     "cssVariables": true
10 |   },
11 |   "aliases": {
12 |     "components": "@/src/components",
13 |     "utils": "@/src/utils/tailwind"
14 |   }
15 | }
16 | 


--------------------------------------------------------------------------------
/web/playwright.config.ts:
--------------------------------------------------------------------------------
 1 | import { defineConfig } from "@playwright/test";
 2 | 
 3 | export default defineConfig({
 4 |   use: {
 5 |     /* Base URL to use in actions like `await page.goto('/')`. */
 6 |     baseURL: "http://localhost:3000",
 7 |   },
 8 |   webServer: {
 9 |     command: process.env.CI ? "npm run start" : "npm run dev",
10 |     url: "http://127.0.0.1:3000",
11 |     reuseExistingServer: !process.env.CI,
12 |     stdout: "ignore",
13 |     stderr: "pipe",
14 |   },
15 | });
16 | 


--------------------------------------------------------------------------------
/web/postcss.config.cjs:
--------------------------------------------------------------------------------
1 | const config = {
2 |   plugins: {
3 |     tailwindcss: {},
4 |     autoprefixer: {},
5 |   },
6 | };
7 | 
8 | module.exports = config;
9 | 


--------------------------------------------------------------------------------
/web/prettier.config.cjs:
--------------------------------------------------------------------------------
1 | /** @type {import("prettier").Config} */
2 | const config = {
3 |   plugins: [require.resolve("prettier-plugin-tailwindcss")],
4 | };
5 | 
6 | module.exports = config;
7 | 


--------------------------------------------------------------------------------
/web/public/android-chrome-192x192.png:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langfuse/langfuse/c8b282dc822c8cec556663f25a000eee58c0dbf6/web/public/android-chrome-192x192.png


--------------------------------------------------------------------------------
/web/public/apple-touch-icon.png:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langfuse/langfuse/c8b282dc822c8cec556663f25a000eee58c0dbf6/web/public/apple-touch-icon.png


--------------------------------------------------------------------------------
/web/public/assets/ragas-logo.png:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langfuse/langfuse/c8b282dc822c8cec556663f25a000eee58c0dbf6/web/public/assets/ragas-logo.png


--------------------------------------------------------------------------------
/web/public/favicon-16x16.png:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langfuse/langfuse/c8b282dc822c8cec556663f25a000eee58c0dbf6/web/public/favicon-16x16.png


--------------------------------------------------------------------------------
/web/public/favicon-32x32.png:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langfuse/langfuse/c8b282dc822c8cec556663f25a000eee58c0dbf6/web/public/favicon-32x32.png


--------------------------------------------------------------------------------
/web/public/favicon.ico:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langfuse/langfuse/c8b282dc822c8cec556663f25a000eee58c0dbf6/web/public/favicon.ico


--------------------------------------------------------------------------------
/web/public/icon256.png:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langfuse/langfuse/c8b282dc822c8cec556663f25a000eee58c0dbf6/web/public/icon256.png


--------------------------------------------------------------------------------
/web/src/__tests__/after-teardown.ts:
--------------------------------------------------------------------------------
1 | import teardown from "@/src/__tests__/teardown";
2 | 
3 | afterAll(async () => {
4 |   await teardown();
5 | });
6 | 


--------------------------------------------------------------------------------
/web/src/__tests__/static/bitcoin.pdf:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langfuse/langfuse/c8b282dc822c8cec556663f25a000eee58c0dbf6/web/src/__tests__/static/bitcoin.pdf


--------------------------------------------------------------------------------
/web/src/__tests__/static/langfuse-logo.png:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langfuse/langfuse/c8b282dc822c8cec556663f25a000eee58c0dbf6/web/src/__tests__/static/langfuse-logo.png


--------------------------------------------------------------------------------
/web/src/__tests__/teardown.ts:
--------------------------------------------------------------------------------
 1 | export default async function teardown() {
 2 |   const { redis, logger } = await import("@langfuse/shared/src/server");
 3 |   logger.debug(`Redis status ${redis?.status}`);
 4 |   if (!redis) {
 5 |     return;
 6 |   }
 7 |   if (redis.status === "end" || redis.status === "close") {
 8 |     logger.debug("Redis connection already closed");
 9 |     return;
10 |   }
11 |   redis?.disconnect();
12 |   logger.debug("Teardown complete");
13 | }
14 | 


--------------------------------------------------------------------------------
/web/src/app/api/billing/stripe-webhook/route.ts:
--------------------------------------------------------------------------------
1 | import { stripeWebhookApiHandler } from "@/src/ee/features/billing/server/stripeWebhookApiHandler";
2 | 
3 | export const dynamic = "force-dynamic";
4 | 
5 | export const POST = stripeWebhookApiHandler;
6 | 


--------------------------------------------------------------------------------
/web/src/app/api/chatCompletion/route.ts:
--------------------------------------------------------------------------------
1 | import chatCompletionHandler from "@/src/features/playground/server/chatCompletionHandler";
2 | 
3 | export const dynamic = "force-dynamic";
4 | export const maxDuration = 120;
5 | 
6 | export const POST = chatCompletionHandler;
7 | 


--------------------------------------------------------------------------------
/web/src/app/layout.tsx:
--------------------------------------------------------------------------------
 1 | export const metadata = {
 2 |   title: 'Next.js',
 3 |   description: 'Generated by Next.js',
 4 | }
 5 | 
 6 | export default function RootLayout({
 7 |   children,
 8 | }: {
 9 |   children: React.ReactNode
10 | }) {
11 |   return (
12 |     <html lang="en">
13 |       <body>{children}</body>
14 |     </html>
15 |   )
16 | }
17 | 


--------------------------------------------------------------------------------
/web/src/components/ChatMessages/utils/createEmptyMessage.ts:
--------------------------------------------------------------------------------
 1 | import { v4 as uuidv4 } from "uuid";
 2 | import { type ChatMessage, type ChatMessageWithId } from "@langfuse/shared";
 3 | 
 4 | export function createEmptyMessage(message: ChatMessage): ChatMessageWithId {
 5 |   return {
 6 |     ...message,
 7 |     content: message.content ?? "",
 8 |     id: uuidv4(),
 9 |   };
10 | }
11 | 


--------------------------------------------------------------------------------
/web/src/components/editor/index.ts:
--------------------------------------------------------------------------------
1 | export * from "./CodeMirrorEditor";
2 | 


--------------------------------------------------------------------------------
/web/src/components/layouts/settings-table-card.tsx:
--------------------------------------------------------------------------------
 1 | import { Card } from "@/src/components/ui/card";
 2 | 
 3 | export const SettingsTableCard = ({
 4 |   children,
 5 | }: {
 6 |   children: React.ReactNode;
 7 | }) => {
 8 |   return (
 9 |     <Card className="mb-4 flex max-h-[60dvh] flex-col overflow-hidden [&>:first-child>:first-child]:border-t-0">
10 |       {children}
11 |     </Card>
12 |   );
13 | };
14 | 


--------------------------------------------------------------------------------
/web/src/components/layouts/spinner.tsx:
--------------------------------------------------------------------------------
 1 | import { LangfuseIcon } from "@/src/components/LangfuseLogo";
 2 | 
 3 | export function Spinner(props: { message: string }) {
 4 |   return (
 5 |     <div className="flex min-h-full flex-1 flex-col justify-center py-12 sm:px-6 lg:px-8">
 6 |       <div className="sm:mx-auto sm:w-full sm:max-w-md">
 7 |         <LangfuseIcon className="mx-auto motion-safe:animate-spin" size={42} />
 8 |         <h2 className="mt-5 text-center text-2xl font-bold leading-9 tracking-tight text-primary">
 9 |           {props.message} ...
10 |         </h2>
11 |       </div>
12 |     </div>
13 |   );
14 | }
15 | 


--------------------------------------------------------------------------------
/web/src/components/level-colors.tsx:
--------------------------------------------------------------------------------
 1 | import { type ObservationLevelType } from "@langfuse/shared";
 2 | 
 3 | export const LevelColors = {
 4 |   DEFAULT: { text: "", bg: "" },
 5 |   DEBUG: { text: "text-muted-foreground", bg: "bg-primary-foreground" },
 6 |   WARNING: { text: "text-dark-yellow", bg: "bg-light-yellow" },
 7 |   ERROR: { text: "text-dark-red", bg: "bg-light-red" },
 8 | };
 9 | 
10 | export const LevelSymbols = {
11 |   DEFAULT: "ℹ️",
12 |   DEBUG: "🔍",
13 |   WARNING: "⚠️",
14 |   ERROR: "🚨",
15 | };
16 | 
17 | export const formatAsLabel = (countLabel: string) => {
18 |   return countLabel.replace(/Count$/, "").toUpperCase() as ObservationLevelType;
19 | };
20 | 


--------------------------------------------------------------------------------
/web/src/components/table/peek/hooks/usePeekEvalConfigData.ts:
--------------------------------------------------------------------------------
 1 | import { api } from "@/src/utils/api";
 2 | 
 3 | type UsePeekEvalConfigDataProps = {
 4 |   projectId: string;
 5 |   jobConfigurationId?: string;
 6 | };
 7 | 
 8 | export const usePeekEvalConfigData = ({
 9 |   projectId,
10 |   jobConfigurationId,
11 | }: UsePeekEvalConfigDataProps) => {
12 |   return api.evals.configById.useQuery(
13 |     {
14 |       id: jobConfigurationId as string,
15 |       projectId,
16 |     },
17 |     {
18 |       enabled: !!jobConfigurationId,
19 |     },
20 |   );
21 | };
22 | 


--------------------------------------------------------------------------------
/web/src/components/table/peek/hooks/usePeekEvalTemplateData.ts:
--------------------------------------------------------------------------------
 1 | import { api } from "@/src/utils/api";
 2 | 
 3 | type UsePeekEvalTemplateDataProps = {
 4 |   projectId: string;
 5 |   templateId?: string;
 6 | };
 7 | 
 8 | export const usePeekEvalTemplateData = ({
 9 |   projectId,
10 |   templateId,
11 | }: UsePeekEvalTemplateDataProps) => {
12 |   return api.evals.templateById.useQuery(
13 |     {
14 |       id: templateId as string,
15 |       projectId,
16 |     },
17 |     {
18 |       enabled: !!templateId,
19 |     },
20 |   );
21 | };
22 | 


--------------------------------------------------------------------------------
/web/src/components/table/table-id.tsx:
--------------------------------------------------------------------------------
 1 | import { cn } from "@/src/utils/tailwind";
 2 | 
 3 | export default function TableIdOrName({
 4 |   value,
 5 |   className,
 6 | }: {
 7 |   value: string;
 8 |   className?: string;
 9 | }) {
10 |   return (
11 |     <div
12 |       title={value}
13 |       className={cn(
14 |         "inline-block max-w-full overflow-hidden text-ellipsis text-nowrap rounded py-0.5 text-xs font-semibold",
15 |         className,
16 |       )}
17 |     >
18 |       {value}
19 |     </div>
20 |   );
21 | }
22 | 


--------------------------------------------------------------------------------
/web/src/components/table/table-view-presets/hooks/useViewData.ts:
--------------------------------------------------------------------------------
 1 | import { api } from "@/src/utils/api";
 2 | 
 3 | type UseViewDataProps = {
 4 |   tableName: string;
 5 |   projectId: string;
 6 | };
 7 | 
 8 | export const useViewData = ({ tableName, projectId }: UseViewDataProps) => {
 9 |   const { data: TableViewPresets } =
10 |     api.TableViewPresets.getByTableName.useQuery({
11 |       tableName,
12 |       projectId,
13 |     });
14 | 
15 |   return {
16 |     TableViewPresetsList: TableViewPresets,
17 |   };
18 | };
19 | 


--------------------------------------------------------------------------------
/web/src/components/ui/collapsible.tsx:
--------------------------------------------------------------------------------
 1 | "use client";
 2 | 
 3 | import * as CollapsiblePrimitive from "@radix-ui/react-collapsible";
 4 | 
 5 | const Collapsible = CollapsiblePrimitive.Root;
 6 | 
 7 | const CollapsibleTrigger = CollapsiblePrimitive.CollapsibleTrigger;
 8 | 
 9 | const CollapsibleContent = CollapsiblePrimitive.CollapsibleContent;
10 | 
11 | export { Collapsible, CollapsibleTrigger, CollapsibleContent };
12 | 


--------------------------------------------------------------------------------
/web/src/components/ui/skeleton.tsx:
--------------------------------------------------------------------------------
 1 | import { cn } from "@/src/utils/tailwind";
 2 | 
 3 | function Skeleton({
 4 |   className,
 5 |   ...props
 6 | }: React.HTMLAttributes<HTMLDivElement>) {
 7 |   return (
 8 |     <div
 9 |       className={cn("animate-pulse rounded-md bg-muted", className)}
10 |       {...props}
11 |     />
12 |   );
13 | }
14 | 
15 | export { Skeleton };
16 | 


--------------------------------------------------------------------------------
/web/src/constants/VERSION.ts:
--------------------------------------------------------------------------------
1 | export const VERSION = "v3.68.0";
2 | 


--------------------------------------------------------------------------------
/web/src/constants/index.ts:
--------------------------------------------------------------------------------
1 | export { VERSION } from "./VERSION";
2 | 


--------------------------------------------------------------------------------
/web/src/ee/README.md:
--------------------------------------------------------------------------------
1 | # Enterprise Edition
2 | 
3 | This folder includes features that are only available in the Enterprise Edition of Langfuse and on Langfuse Cloud.
4 | 
5 | See [LICENSE](../../../LICENSE) and [docs](https://langfuse.com/docs/open-source) for more details.
6 | 


--------------------------------------------------------------------------------
/web/src/ee/features/billing/constants.ts:
--------------------------------------------------------------------------------
1 | export const MAX_EVENTS_FREE_PLAN = 50_000;
2 | 


--------------------------------------------------------------------------------
/web/src/ee/features/billing/utils/stripe.ts:
--------------------------------------------------------------------------------
1 | import { env } from "@/src/env.mjs";
2 | import Stripe from "stripe";
3 | 
4 | export const stripeClient =
5 |   env.STRIPE_SECRET_KEY && env.NEXT_PUBLIC_LANGFUSE_CLOUD_REGION
6 |     ? new Stripe(env.STRIPE_SECRET_KEY)
7 |     : undefined;
8 | 


--------------------------------------------------------------------------------
/web/src/ee/features/multi-tenant-sso/multiTenantSsoAvailable.ts:
--------------------------------------------------------------------------------
1 | import { env } from "@/src/env.mjs";
2 | 
3 | export const multiTenantSsoAvailable = Boolean(
4 |   env.NEXT_PUBLIC_LANGFUSE_CLOUD_REGION,
5 | );
6 | 


--------------------------------------------------------------------------------
/web/src/features/auth/hooks.ts:
--------------------------------------------------------------------------------
 1 | import { useSession } from "next-auth/react";
 2 | 
 3 | /**
 4 |  * Hook to check if the user is authenticated and a member of the project.
 5 |  */
 6 | export const useIsAuthenticatedAndProjectMember = (
 7 |   projectId: string,
 8 | ): boolean => {
 9 |   const session = useSession();
10 | 
11 |   if (projectId === "") return false;
12 | 
13 |   return (
14 |     session.status === "authenticated" &&
15 |     !!session.data?.user?.organizations
16 |       .flatMap((org) => org.projects)
17 |       .find(({ id }) => id === projectId)
18 |   );
19 | };
20 | 


--------------------------------------------------------------------------------
/web/src/features/auth/lib/projectNameSchema.ts:
--------------------------------------------------------------------------------
 1 | import { noHtmlCheck } from "@langfuse/shared";
 2 | import * as z from "zod/v4";
 3 | 
 4 | export const projectNameSchema = z.object({
 5 |   name: z
 6 |     .string()
 7 |     .min(3, "Must have at least 3 characters")
 8 |     .max(60, "Must have at most 60 characters")
 9 |     .refine((value) => noHtmlCheck(value), {
10 |       message: "Input should not contain HTML",
11 |     }),
12 | });
13 | 


--------------------------------------------------------------------------------
/web/src/features/auth/lib/projectRetentionSchema.ts:
--------------------------------------------------------------------------------
 1 | import * as z from "zod/v4";
 2 | 
 3 | export const projectRetentionSchema = z.object({
 4 |   retention: z.coerce
 5 |     .number()
 6 |     .int("Must be an integer")
 7 |     .refine((value) => value === 0 || value >= 3, {
 8 |       message: "Value must be 0 or at least 3 days",
 9 |     }),
10 | });
11 | 


--------------------------------------------------------------------------------
/web/src/features/batch-exports/README.md:
--------------------------------------------------------------------------------
1 | # Batch Exports
2 | 
3 | - Find types in shared
4 | - Actual export logic in worker
5 | 


--------------------------------------------------------------------------------
/web/src/features/cloud-status-notification/types.ts:
--------------------------------------------------------------------------------
1 | import { z } from "zod/v4";
2 | 
3 | export const CloudStatus = z
4 |   .enum(["operational", "downtime", "degraded", "maintenance"])
5 |   .nullable();
6 | 
7 | export type CloudStatus = z.infer<typeof CloudStatus>;
8 | 


--------------------------------------------------------------------------------
/web/src/features/dashboard/components/LeftAlignedCell.tsx:
--------------------------------------------------------------------------------
 1 | import { cn } from "@/src/utils/tailwind";
 2 | import { type ReactNode } from "react";
 3 | 
 4 | export const LeftAlignedCell = ({
 5 |   children,
 6 |   className,
 7 |   title,
 8 | }: {
 9 |   children: ReactNode;
10 |   className?: string;
11 |   title?: string;
12 | }) => (
13 |   <div className={cn("text-left", className)} title={title}>
14 |     {children}
15 |   </div>
16 | );
17 | 


--------------------------------------------------------------------------------
/web/src/features/dashboard/components/RightAlignedCell.tsx:
--------------------------------------------------------------------------------
 1 | import { cn } from "@/src/utils/tailwind";
 2 | import { type ReactNode } from "react";
 3 | 
 4 | export const RightAlignedCell = ({
 5 |   children,
 6 |   className,
 7 |   title,
 8 | }: {
 9 |   children: ReactNode;
10 |   className?: string;
11 |   title?: string;
12 | }) => (
13 |   <div className={cn("text-right", className)} title={title}>
14 |     {children}
15 |   </div>
16 | );
17 | 


--------------------------------------------------------------------------------
/web/src/features/evals/components/ragas-logo.tsx:
--------------------------------------------------------------------------------
 1 | export const RagasLogoIcon = () => {
 2 |   return (
 3 |     <div className="flex items-center">
 4 |       {/* eslint-disable-next-line @next/next/no-img-element */}
 5 |       <img
 6 |         src="/assets/ragas-logo.png"
 7 |         alt="Ragas Logo"
 8 |         width={12}
 9 |         height={12}
10 |       />
11 |     </div>
12 |   );
13 | };
14 | 


--------------------------------------------------------------------------------
/web/src/features/evals/hooks/useValidateCustomModel.ts:
--------------------------------------------------------------------------------
 1 | import { type ModelParams } from "@langfuse/shared";
 2 | 
 3 | export function useValidateCustomModel(
 4 |   availableProviders: string[],
 5 |   customModelParams?: {
 6 |     provider: string;
 7 |     model: string;
 8 |     modelParams: ModelParams & {
 9 |       maxTemperature: number;
10 |     };
11 |   },
12 | ): { isCustomModelValid: boolean } {
13 |   if (!customModelParams) {
14 |     return { isCustomModelValid: false };
15 |   }
16 | 
17 |   if (!availableProviders.includes(customModelParams.provider)) {
18 |     return { isCustomModelValid: false };
19 |   }
20 | 
21 |   return { isCustomModelValid: true };
22 | }
23 | 


--------------------------------------------------------------------------------
/web/src/features/feature-flags/README.md:
--------------------------------------------------------------------------------
 1 | # Feature Flags
 2 | 
 3 | Configure feature flags in the `available-flags.ts` file.
 4 | 
 5 | Use the `useIsFeatureEnabled` hook to check if a feature flag is enabled.
 6 | 
 7 | ```tsx
8 | const isFeatureEnabled = useIsFeatureEnabled("feature-flag-name");
 9 |
```
10 | 
11 | When is a feature flag enabled?
12 | 
13 | 1. flag is in user.feature_flags
14 | 2. LANGFUSE_ENABLE_EXPERIMENTAL_FEATURES is set
15 | 3. user.admin is true
16 | 


--------------------------------------------------------------------------------
/web/src/features/feature-flags/available-flags.ts:
--------------------------------------------------------------------------------
1 | export const availableFlags = [
2 |   "templateFlag",
3 |   "excludeClickhouseRead",
4 | ] as const;
5 | 


--------------------------------------------------------------------------------
/web/src/features/feature-flags/hooks/useIsFeatureEnabled.ts:
--------------------------------------------------------------------------------
 1 | import { useSession } from "next-auth/react";
 2 | import type { Flag } from "../types";
 3 | 
 4 | export default function useIsFeatureEnabled(feature: Flag): boolean {
 5 |   const session = useSession();
 6 | 
 7 |   const isAdmin = session.data?.user?.admin ?? false;
 8 | 
 9 |   const isExperimentalFeaturesEnabled =
10 |     session.data?.environment.enableExperimentalFeatures ?? false;
11 | 
12 |   const isFeatureEnabledOnUser =
13 |     session.data?.user?.featureFlags[feature] ?? false;
14 | 
15 |   return isExperimentalFeaturesEnabled || isAdmin || isFeatureEnabledOnUser;
16 | }
17 | 


--------------------------------------------------------------------------------
/web/src/features/feature-flags/types.ts:
--------------------------------------------------------------------------------
1 | import { type availableFlags } from "./available-flags";
2 | 
3 | export type Flag = (typeof availableFlags)[number];
4 | export type Flags = {
5 |   [key in (typeof availableFlags)[number]]: boolean;
6 | };
7 | 


--------------------------------------------------------------------------------
/web/src/features/feature-flags/utils.ts:
--------------------------------------------------------------------------------
 1 | import { availableFlags } from "./available-flags";
 2 | import { type Flags } from "./types";
 3 | 
 4 | export const parseFlags = (dbFlags: string[]): Flags => {
 5 |   const parsedFlags = {} as Flags;
 6 | 
 7 |   availableFlags.forEach((flag) => {
 8 |     parsedFlags[flag] = dbFlags.includes(flag);
 9 |   });
10 | 
11 |   return parsedFlags;
12 | };
13 | 


--------------------------------------------------------------------------------
/web/src/features/models/components/ModelSettings.tsx:
--------------------------------------------------------------------------------
 1 | import Header from "@/src/components/layouts/header";
 2 | import ModelTable from "@/src/components/table/use-cases/models";
 3 | 
 4 | export function ModelsSettings(props: { projectId: string }) {
 5 |   return (
 6 |     <>
 7 |       <Header title="Models" />
 8 |       <p className="mb-2 text-sm">
 9 |         A model represents a LLM model. It is used to calculate tokens and cost.
10 |       </p>
11 |       <ModelTable projectId={props.projectId} />
12 |     </>
13 |   );
14 | }
15 | 


--------------------------------------------------------------------------------
/web/src/features/models/server/isValidPostgresRegex.ts:
--------------------------------------------------------------------------------
 1 | import { Prisma, type prisma as _prisma } from "@langfuse/shared/src/db";
 2 | 
 3 | export const isValidPostgresRegex = async (
 4 |   regex: string,
 5 |   prisma: typeof _prisma,
 6 | ): Promise<boolean> => {
 7 |   try {
 8 |     await prisma.$queryRaw(Prisma.sql`SELECT 'test_string' ~ ${regex}`);
 9 |     return true;
10 |   } catch {
11 |     return false;
12 |   }
13 | };
14 | 


--------------------------------------------------------------------------------
/web/src/features/models/utils.ts:
--------------------------------------------------------------------------------
 1 | import Decimal from "decimal.js";
 2 | 
 3 | export const getMaxDecimals = (
 4 |   value: number | undefined,
 5 |   scaleMultiplier: number = 1,
 6 | ) => {
 7 |   return (
 8 |     new Decimal(value ?? 0)
 9 |       .mul(scaleMultiplier)
10 |       .toFixed(12)
11 |       .split(".")[1]
12 |       ?.replace(/0+$/, "").length ?? 0
13 |   );
14 | };
15 | 


--------------------------------------------------------------------------------
/web/src/features/organizations/utils/organizationNameSchema.ts:
--------------------------------------------------------------------------------
 1 | import { noHtmlCheck } from "@langfuse/shared";
 2 | import * as z from "zod/v4";
 3 | 
 4 | export const organizationNameSchema = z.object({
 5 |   name: z
 6 |     .string()
 7 |     .min(3, "Must have at least 3 characters")
 8 |     .max(60, "Must have at most 60 characters")
 9 |     .refine((value) => noHtmlCheck(value), {
10 |       message: "Input should not contain HTML",
11 |     }),
12 | });
13 | 


--------------------------------------------------------------------------------
/web/src/features/playground/page/hooks/useCommandEnter.ts:
--------------------------------------------------------------------------------
 1 | import { useEffect } from "react";
 2 | 
 3 | export default function useCommandEnter(
 4 |   isEnabled: boolean,
 5 |   callback: () => Promise<void>,
 6 | ) {
 7 |   useEffect(() => {
 8 |     function handleKeyDown(event: KeyboardEvent) {
 9 |       if (
10 |         isEnabled &&
11 |         (event.metaKey || event.ctrlKey) &&
12 |         event.code === "Enter"
13 |       ) {
14 |         callback().catch((err) => console.error(err));
15 |       }
16 |     }
17 | 
18 |     document.addEventListener("keydown", handleKeyDown);
19 | 
20 |     return () => document.removeEventListener("keydown", handleKeyDown);
21 |   }, [isEnabled, callback]);
22 | }
23 | 


--------------------------------------------------------------------------------
/web/src/features/posthog-analytics/ServerPosthog.ts:
--------------------------------------------------------------------------------
 1 | import { env } from "@/src/env.mjs";
 2 | import { PostHog as OriginalPosthog } from "posthog-node";
 3 | 
 4 | // Safe as it is intended to be public
 5 | const PUBLIC_POSTHOG_API_KEY =
 6 |   env.NEXT_PUBLIC_POSTHOG_KEY ||
 7 |   "phc_zkMwFajk8ehObUlMth0D7DtPItFnxETi3lmSvyQDrwB";
 8 | const POSTHOG_HOST = env.NEXT_PUBLIC_POSTHOG_HOST || "https://eu.posthog.com";
 9 | 
10 | export class ServerPosthog extends OriginalPosthog {
11 |   constructor() {
12 |     super(PUBLIC_POSTHOG_API_KEY, {
13 |       host: POSTHOG_HOST,
14 |     });
15 | 
16 |     if (process.env.NODE_ENV === "development") this.debug();
17 |   }
18 | }
19 | 


--------------------------------------------------------------------------------
/web/src/features/posthog-integration/types.ts:
--------------------------------------------------------------------------------
 1 | import { z } from "zod/v4";
 2 | 
 3 | export const posthogIntegrationFormSchema = z.object({
 4 |   posthogHostname: z.string().url(),
 5 |   posthogProjectApiKey: z.string().refine((v) => v.startsWith("phc_"), {
 6 |     message:
 7 |       "PostHog 'Project API Key' must start with 'phc_'. You can find it in the PostHog project settings.",
 8 |   }),
 9 |   enabled: z.boolean(),
10 | });
11 | 


--------------------------------------------------------------------------------
/web/src/features/prompts/constants.ts:
--------------------------------------------------------------------------------
1 | export const PRODUCTION_LABEL = "production";
2 | export const LATEST_PROMPT_LABEL = "latest";
3 | export const COMMIT_MESSAGE_MAX_LENGTH = 500;
4 | 


--------------------------------------------------------------------------------
/web/src/features/prompts/utils.ts:
--------------------------------------------------------------------------------
1 | import {
2 |   LATEST_PROMPT_LABEL,
3 |   PRODUCTION_LABEL,
4 | } from "@/src/features/prompts/constants";
5 | 
6 | export const isReservedPromptLabel = (label: string) => {
7 |   return [PRODUCTION_LABEL, LATEST_PROMPT_LABEL].includes(label);
8 | };
9 | 


--------------------------------------------------------------------------------
/web/src/features/public-api/types/events.ts:
--------------------------------------------------------------------------------
1 | import { z } from "zod/v4";
2 | import { CreateEventEvent } from "@langfuse/shared/src/server";
3 | 
4 | // POST /events
5 | export const PostEventsV1Body = CreateEventEvent;
6 | export const PostEventsV1Response = z.object({ id: z.string() });
7 | 


--------------------------------------------------------------------------------
/web/src/features/public-api/types/generations.ts:
--------------------------------------------------------------------------------
 1 | // src/features/public-api/types/generations.ts
 2 | 
 3 | import { z } from "zod/v4";
 4 | import {
 5 |   LegacyGenerationsCreateSchema,
 6 |   LegacyGenerationPatchSchema,
 7 | } from "@langfuse/shared/src/server";
 8 | 
 9 | // POST /generations
10 | export const PostGenerationsV1Body = LegacyGenerationsCreateSchema;
11 | export const PostGenerationsV1Response = z.object({ id: z.string() });
12 | 
13 | // PATCH /generations
14 | export const PatchGenerationsV1Body = LegacyGenerationPatchSchema;
15 | export const PatchGenerationsV1Response = z.object({ id: z.string() });
16 | 


--------------------------------------------------------------------------------
/web/src/features/public-api/types/spans.ts:
--------------------------------------------------------------------------------
 1 | import { z } from "zod/v4";
 2 | import {
 3 |   LegacySpanPatchSchema,
 4 |   LegacySpanPostSchema,
 5 | } from "@langfuse/shared/src/server";
 6 | 
 7 | // POST /spans
 8 | export const PostSpansV1Body = LegacySpanPostSchema;
 9 | export const PostSpansV1Response = z.object({ id: z.string() });
10 | 
11 | // PATCH /spans
12 | export const PatchSpansV1Body = LegacySpanPatchSchema;
13 | export const PatchSpansV1Response = z.object({ id: z.string() });
14 | 


--------------------------------------------------------------------------------
/web/src/features/query/index.ts:
--------------------------------------------------------------------------------
1 | export * from "./dataModel";
2 | export * from "./dashboardUiTableToViewMapping";
3 | export * from "./types";
4 | 


--------------------------------------------------------------------------------
/web/src/features/rbac/constants/orderedRoles.ts:
--------------------------------------------------------------------------------
 1 | import { Role } from "@langfuse/shared";
 2 | 
 3 | export const orderedRoles: Record<Role, number> = {
 4 |   [Role.OWNER]: 4,
 5 |   [Role.ADMIN]: 3,
 6 |   [Role.MEMBER]: 2,
 7 |   [Role.VIEWER]: 1,
 8 |   [Role.NONE]: 0,
 9 | };
10 | 


--------------------------------------------------------------------------------
/web/src/features/scores/hooks/useScoreCustomOptimistic.ts:
--------------------------------------------------------------------------------
 1 | import { useCallback, useState } from "react";
 2 | 
 3 | export function useScoreCustomOptimistic<State, Action>(
 4 |   initialState: State,
 5 |   reducer: (state: State, action: Action) => State,
 6 | ): [State, (action: Action) => void] {
 7 |   const [state, setState] = useState<State>(initialState);
 8 | 
 9 |   const dispatch = useCallback(
10 |     (action: Action) => {
11 |       setState((currentState) => reducer(currentState, action));
12 |     },
13 |     [reducer],
14 |   );
15 | 
16 |   return [state, dispatch];
17 | }
18 | 


--------------------------------------------------------------------------------
/web/src/features/scores/schema.ts:
--------------------------------------------------------------------------------
 1 | import { ScoreDataType } from "@langfuse/shared";
 2 | import { z } from "zod/v4";
 3 | 
 4 | export const AnnotationScoreDataSchema = z.object({
 5 |   name: z.string(),
 6 |   scoreId: z.string().optional(),
 7 |   value: z.number().nullable().optional(),
 8 |   stringValue: z.string().optional(),
 9 |   dataType: z.enum(ScoreDataType),
10 |   configId: z.string().optional(),
11 |   comment: z.string().optional(),
12 | });
13 | 
14 | export const AnnotateFormSchema = z.object({
15 |   scoreData: z.array(AnnotationScoreDataSchema),
16 | });
17 | 


--------------------------------------------------------------------------------
/web/src/features/setup/setupRoutes.ts:
--------------------------------------------------------------------------------
 1 | export const createOrganizationRoute = "/setup";
 2 | 
 3 | export const createProjectRoute = (orgId: string) =>
 4 |   `/organization/${orgId}/setup?orgstep=create-project`;
 5 | 
 6 | export const inviteMembersRoute = (orgId: string) =>
 7 |   `/organization/${orgId}/setup?orgstep=invite-members`;
 8 | 
 9 | export const setupTracingRoute = (projectId: string) =>
10 |   `/project/${projectId}/setup`;
11 | 


--------------------------------------------------------------------------------
/web/src/features/slack/server/slack-webhook.ts:
--------------------------------------------------------------------------------
 1 | import { env } from "@/src/env.mjs";
 2 | 
 3 | export const sendToSlack = async (message: unknown) => {
 4 |   if (!env.LANGFUSE_TEAM_SLACK_WEBHOOK)
 5 |     throw new Error("LANGFUSE_TEAM_SLACK_WEBHOOK is not set");
 6 | 
 7 |   return await fetch(env.LANGFUSE_TEAM_SLACK_WEBHOOK, {
 8 |     method: "POST",
 9 |     body: JSON.stringify({ rawBody: JSON.stringify(message, null, 2) }),
10 |     headers: {
11 |       "Content-Type": "application/json",
12 |     },
13 |   });
14 | };
15 | 


--------------------------------------------------------------------------------
/web/src/features/support-chat/createSupportEmailHash.ts:
--------------------------------------------------------------------------------
 1 | import { env } from "@/src/env.mjs";
 2 | import { logger } from "@langfuse/shared/src/server";
 3 | import * as crypto from "node:crypto";
 4 | 
 5 | export const createSupportEmailHash = (email: string): string | undefined => {
 6 |   if (!env.PLAIN_AUTHENTICATION_SECRET) {
 7 |     if (env.NEXT_PUBLIC_LANGFUSE_CLOUD_REGION) {
 8 |       logger.error("PLAIN_AUTHENTICATION_SECRET is not set");
 9 |     }
10 |     return undefined;
11 |   }
12 |   const hmac = crypto.createHmac("sha256", env.PLAIN_AUTHENTICATION_SECRET);
13 |   hmac.update(email);
14 |   const hash = hmac.digest("hex");
15 |   return hash;
16 | };
17 | 


--------------------------------------------------------------------------------
/web/src/features/table/components/targetOptionsQueryMap.tsx:
--------------------------------------------------------------------------------
1 | import { api } from "@/src/utils/api";
2 | 
3 | export const targetOptionsQueryMap = {
4 |   "trace-add-to-annotation-queue": api.annotationQueues.allNamesAndIds.useQuery,
5 | } as const;
6 | 


--------------------------------------------------------------------------------
/web/src/features/table/server/helpers.ts:
--------------------------------------------------------------------------------
1 | export const generateBatchActionId = (
2 |   projectId: string,
3 |   actionId: string,
4 |   tableName: string,
5 | ) => {
6 |   return `${projectId}-${tableName}-${actionId}`;
7 | };
8 | 


--------------------------------------------------------------------------------
/web/src/features/telemetry/README.md:
--------------------------------------------------------------------------------
 1 | # Telemetry service for Docker deployments
 2 | 
 3 | By default, Langfuse automatically reports basic usage statistics to a centralized server (PostHog).
 4 | 
 5 | This helps us to:
 6 | 
 7 | 1. Understand how Langfuse is used and improve the most relevant features.
 8 | 2. Track overall usage for internal and external (e.g. fundraising) reporting.
 9 | 
10 | None of the data is shared with third parties and does not include any sensitive information. We want to be super transparent about this and you can find the exact data we collect [here](/src/features/telemetry/index.ts).
11 | 
12 | You can opt-out by setting `TELEMETRY_ENABLED=false`.
13 | 


--------------------------------------------------------------------------------
/web/src/features/theming/ThemeProvider.tsx:
--------------------------------------------------------------------------------
 1 | "use client";
 2 | 
 3 | import * as React from "react";
 4 | import { ThemeProvider as NextThemesProvider } from "next-themes";
 5 | import { type ThemeProviderProps } from "next-themes/dist/types";
 6 | 
 7 | export function ThemeProvider({ children, ...props }: ThemeProviderProps) {
 8 |   return <NextThemesProvider {...props}>{children}</NextThemesProvider>;
 9 | }
10 | 


--------------------------------------------------------------------------------
/web/src/features/widgets/chart-library/chart-props.ts:
--------------------------------------------------------------------------------
 1 | import { type ChartConfig } from "@/src/components/ui/chart";
 2 | 
 3 | export interface DataPoint {
 4 |   time_dimension: string | undefined;
 5 |   dimension: string | undefined;
 6 |   metric: number | Array<Array<number>>;
 7 | }
 8 | 
 9 | export interface ChartProps {
10 |   data: DataPoint[];
11 |   config?: ChartConfig;
12 |   accessibilityLayer?: boolean;
13 | }
14 | 


--------------------------------------------------------------------------------
/web/src/features/widgets/index.ts:
--------------------------------------------------------------------------------
1 | // Export the DataPoint type
2 | export { type DataPoint } from "./chart-library/chart-props";
3 | export { Chart } from "./chart-library/Chart";
4 | 
5 | // Export components
6 | export { WidgetForm } from "./components/WidgetForm";
7 | export { DashboardWidgetTable, DeleteWidget } from "./components/WidgetTable";
8 | export { DashboardWidget } from "./components/DashboardWidget";
9 | 


--------------------------------------------------------------------------------
/web/src/hooks/useProjectIdFromURL.ts:
--------------------------------------------------------------------------------
1 | import { useRouter } from "next/router";
2 | 
3 | export default function useProjectIdFromURL() {
4 |   const router = useRouter();
5 | 
6 |   return router.query.projectId as string | undefined;
7 | }
8 | 


--------------------------------------------------------------------------------
/web/src/instrumentation.ts:
--------------------------------------------------------------------------------
 1 | // See: https://vercel.com/docs/observability/otel-overview
 2 | export async function register() {
 3 |   // This variable is set in the .env file or environment variables
 4 |   // Value is true if NEXT_PUBLIC_LANGFUSE_RUN_NEXT_INIT is "true" or undefined
 5 |   const isInitLoadingEnabled =
 6 |     process.env.NEXT_PUBLIC_LANGFUSE_RUN_NEXT_INIT !== undefined
 7 |       ? process.env.NEXT_PUBLIC_LANGFUSE_RUN_NEXT_INIT === "true"
 8 |       : true;
 9 | 
10 |   if (process.env.NEXT_RUNTIME === "nodejs" && isInitLoadingEnabled) {
11 |     console.log("Running init scripts...");
12 |     await import("./observability.config");
13 |     await import("./initialize");
14 |   }
15 | }
16 | 


--------------------------------------------------------------------------------
/web/src/pages/api/auth/add-sso-config.ts:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * This endpoint is used to add a new SSO configuration to the database.
 3 |  *
 4 |  * This is an EE feature and will return a 404 response if EE is not available.
 5 |  */
 6 | 
 7 | import { createNewSsoConfigHandler } from "@/src/ee/features/multi-tenant-sso/createNewSsoConfigHandler";
 8 | 
 9 | export default createNewSsoConfigHandler;
10 | 


--------------------------------------------------------------------------------
/web/src/pages/api/auth/signup.ts:
--------------------------------------------------------------------------------
1 | import { signupApiHandler } from "@/src/features/auth-credentials/server/signupApiHandler";
2 | 
3 | export default signupApiHandler;
4 | 


--------------------------------------------------------------------------------
/web/src/pages/api/billing/README.md:
--------------------------------------------------------------------------------
1 | These APIs are implemented via the NextJS App router in src/app/api/billing.
2 | 


--------------------------------------------------------------------------------
/web/src/pages/api/feedback.ts:
--------------------------------------------------------------------------------
1 | import feedbackApiHandler from "@/src/features/feedback/server/feedbackHandler";
2 | 
3 | export default feedbackApiHandler;
4 | 


--------------------------------------------------------------------------------
/web/src/pages/api/public/otel/otlp-proto/README.md:
--------------------------------------------------------------------------------
1 | # otlp-proto
2 | 
3 | This directory contains compiled opentelemetry protobuf files.
4 | Those should correspond to the definitions in https://github.com/open-telemetry/opentelemetry-proto/tree/v1.5.0 and are copied
5 | from the generated contents of https://www.npmjs.com/package/@opentelemetry/otlp-transformer.
6 | The file was converted from `.js` to `.ts` and the `export` statements were modified to make them Next.js compatible.
7 | 
8 | Unless there are relevant updates to the OpenTelemetry specification, there should be no need to ever touch this.
9 | 


--------------------------------------------------------------------------------
/web/src/pages/api/public/otel/v1/metrics/index.ts:
--------------------------------------------------------------------------------
 1 | import { withMiddlewares } from "@/src/features/public-api/server/withMiddlewares";
 2 | import { createAuthedProjectAPIRoute } from "@/src/features/public-api/server/createAuthedProjectAPIRoute";
 3 | import { z } from "zod/v4";
 4 | 
 5 | export const config = {
 6 |   api: {
 7 |     bodyParser: false,
 8 |   },
 9 | };
10 | 
11 | export default withMiddlewares({
12 |   POST: createAuthedProjectAPIRoute({
13 |     name: "OTel Metrics",
14 |     querySchema: z.any(),
15 |     responseSchema: z.any(),
16 |     rateLimitResource: "ingestion",
17 |     fn: async () => {},
18 |   }),
19 | });
20 | 


--------------------------------------------------------------------------------
/web/src/pages/api/public/v2/prompts/[promptName]/index.ts:
--------------------------------------------------------------------------------
1 | export { promptNameHandler as default } from "@/src/features/prompts/server/handlers/promptNameHandler";
2 | 


--------------------------------------------------------------------------------
/web/src/pages/api/public/v2/prompts/[promptName]/versions/[promptVersion].ts:
--------------------------------------------------------------------------------
1 | export { promptVersionHandler as default } from "@/src/features/prompts/server/handlers/promptVersionHandler";
2 | 


--------------------------------------------------------------------------------
/web/src/pages/api/public/v2/prompts/index.ts:
--------------------------------------------------------------------------------
1 | export { promptsHandler as default } from "@/src/features/prompts/server/handlers/promptsHandler";
2 | 


--------------------------------------------------------------------------------
/web/src/pages/auth/error.tsx:
--------------------------------------------------------------------------------
 1 | import { ErrorPageWithSentry } from "@/src/components/error-page";
 2 | import { useRouter } from "next/router";
 3 | 
 4 | export default function AuthError() {
 5 |   const router = useRouter();
 6 |   const { error } = router.query;
 7 |   const errorMessage = error
 8 |   ? decodeURIComponent(String(error))
 9 |     : "An authentication error occurred. Please reach out to support.";
10 | 
11 |   return (
12 |     <ErrorPageWithSentry title="Authentication Error" message={errorMessage} />
13 |   );
14 | }
15 | 


--------------------------------------------------------------------------------
/web/src/pages/background-migrations.tsx:
--------------------------------------------------------------------------------
1 | import BackgroundMigrationsTable from "@/src/features/background-migrations/components/background-migrations";
2 | 
3 | export default function BackgroundMigrationsPage() {
4 |   return <BackgroundMigrationsTable />;
5 | }
6 | 


--------------------------------------------------------------------------------
/web/src/pages/index.tsx:
--------------------------------------------------------------------------------
1 | import { OrganizationProjectOverview } from "@/src/features/organizations/components/ProjectOverview";
2 | 
3 | export default function Home() {
4 |   return <OrganizationProjectOverview />;
5 | }
6 | 


--------------------------------------------------------------------------------
/web/src/pages/organization/[organizationId]/index.tsx:
--------------------------------------------------------------------------------
1 | export { OrganizationProjectOverview as default } from "@/src/features/organizations/components/ProjectOverview";
2 | 


--------------------------------------------------------------------------------
/web/src/pages/organization/[organizationId]/settings/[page].tsx:
--------------------------------------------------------------------------------
1 | import OrgSettingsPage from "@/src/pages/organization/[organizationId]/settings";
2 | 
3 | export default OrgSettingsPage;
4 | 


--------------------------------------------------------------------------------
/web/src/pages/organization/[organizationId]/setup.tsx:
--------------------------------------------------------------------------------
1 | import { SetupPage } from "@/src/features/setup/components/SetupPage";
2 | 
3 | export default SetupPage;
4 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/annotation-queues.tsx:
--------------------------------------------------------------------------------
1 | import AnnotationQueues from "@/src/features/annotation-queues/pages/AnnotationQueues";
2 | 
3 | export default AnnotationQueues;
4 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/annotation-queues/[queueId]/index.tsx:
--------------------------------------------------------------------------------
1 | import QueueItems from "@/src/features/annotation-queues/pages/AnnotationQueueItems";
2 | 
3 | export default QueueItems;
4 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/annotation-queues/[queueId]/items/[itemId].tsx:
--------------------------------------------------------------------------------
 1 | import { AnnotationQueuesItem } from "@/src/features/annotation-queues/components/AnnotationQueuesItem";
 2 | import { useRouter } from "next/router";
 3 | 
 4 | export default function AnnotationQueues() {
 5 |   const router = useRouter();
 6 |   const annotationQueueId = router.query.queueId as string;
 7 |   const projectId = router.query.projectId as string;
 8 |   const itemId = router.query.itemId as string;
 9 | 
10 |   return (
11 |     <AnnotationQueuesItem
12 |       annotationQueueId={annotationQueueId}
13 |       projectId={projectId}
14 |       itemId={itemId}
15 |     />
16 |   );
17 | }
18 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/annotation-queues/[queueId]/items/index.tsx:
--------------------------------------------------------------------------------
 1 | import { AnnotationQueuesItem } from "@/src/features/annotation-queues/components/AnnotationQueuesItem";
 2 | import { useRouter } from "next/router";
 3 | 
 4 | export default function AnnotationQueues() {
 5 |   const router = useRouter();
 6 |   const annotationQueueId = router.query.queueId as string;
 7 |   const projectId = router.query.projectId as string;
 8 | 
 9 |   return (
10 |     <AnnotationQueuesItem
11 |       annotationQueueId={annotationQueueId}
12 |       projectId={projectId}
13 |     />
14 |   );
15 | }
16 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/evals/[evaluatorId].tsx:
--------------------------------------------------------------------------------
1 | import { EvaluatorDetail } from "@/src/features/evals/components/evaluator-detail";
2 | 
3 | export default EvaluatorDetail;
4 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/evals/default-model.tsx:
--------------------------------------------------------------------------------
1 | export { default as default } from "@/src/features/evals/pages/default-evaluation-model";
2 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/evals/index.tsx:
--------------------------------------------------------------------------------
1 | export { default as default } from "@/src/features/evals/pages/evaluators";
2 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/evals/new.tsx:
--------------------------------------------------------------------------------
1 | export { default as default } from "@/src/features/evals/pages/new-evaluator";
2 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/evals/templates/[id].tsx:
--------------------------------------------------------------------------------
1 | import { EvalTemplateDetail } from "@/src/features/evals/components/eval-template-detail";
2 | 
3 | export default EvalTemplateDetail;
4 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/evals/templates/index.tsx:
--------------------------------------------------------------------------------
1 | export { default as default } from "@/src/features/evals/pages/templates";
2 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/evals/templates/new.tsx:
--------------------------------------------------------------------------------
1 | export { default as default } from "@/src/features/evals/pages/new-template";
2 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/models.tsx:
--------------------------------------------------------------------------------
 1 | import { useRouter } from "next/router";
 2 | import { useEffect } from "react";
 3 | 
 4 | export default function ModelsPage() {
 5 |   const router = useRouter();
 6 |   const projectId = router.query.projectId as string;
 7 | 
 8 |   // temporarily redirect to settings/models
 9 |   useEffect(() => {
10 |     router.replace(`/project/${projectId}/settings/models`);
11 |   }, [projectId, router]);
12 | 
13 |   return null;
14 | }
15 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/playground.tsx:
--------------------------------------------------------------------------------
1 | export { default as default } from "@/src/features/playground/page";
2 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/prompts/[promptName]/index.tsx:
--------------------------------------------------------------------------------
1 | import { PromptDetail } from "@/src/features/prompts/components/prompt-detail";
2 | 
3 | export default PromptDetail;
4 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/prompts/new.tsx:
--------------------------------------------------------------------------------
1 | import { NewPrompt } from "@/src/features/prompts/components/prompt-new";
2 | 
3 | export default NewPrompt;
4 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/sessions/[sessionId].tsx:
--------------------------------------------------------------------------------
 1 | import { useRouter } from "next/router";
 2 | import { SessionPage } from "@/src/components/session";
 3 | 
 4 | export default function Trace() {
 5 |   const router = useRouter();
 6 |   const sessionId = router.query.sessionId as string;
 7 |   const projectId = router.query.projectId as string;
 8 | 
 9 |   return <SessionPage sessionId={sessionId} projectId={projectId} />;
10 | }
11 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/settings/[page].tsx:
--------------------------------------------------------------------------------
1 | import SettingsPage from "@/src/pages/project/[projectId]/settings";
2 | 
3 | export default SettingsPage;
4 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/settings/billing.ts:
--------------------------------------------------------------------------------
 1 | import { useQueryProject } from "@/src/features/projects/hooks";
 2 | import { useRouter } from "next/router";
 3 | import { useEffect } from "react";
 4 | 
 5 | export default function ProjectBillingRedirect() {
 6 |   const router = useRouter();
 7 | 
 8 |   const { organization } = useQueryProject();
 9 | 
10 |   useEffect(() => {
11 |     if (organization) {
12 |       router.replace(`/organization/${organization.id}/settings/billing`);
13 |     }
14 |   }, [organization, router]);
15 | 
16 |   return "Redirecting...";
17 | }
18 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/setup.tsx:
--------------------------------------------------------------------------------
1 | import { SetupPage } from "@/src/features/setup/components/SetupPage";
2 | 
3 | export default SetupPage;
4 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/traces/[traceId].tsx:
--------------------------------------------------------------------------------
 1 | import { TracePage } from "@/src/components/trace/TracePage";
 2 | import { useRouter } from "next/router";
 3 | 
 4 | export default function Trace() {
 5 |   const router = useRouter();
 6 |   const traceId = router.query.traceId as string;
 7 | 
 8 |   const timestamp =
 9 |     router.query.timestamp && typeof router.query.timestamp === "string"
10 |       ? new Date(decodeURIComponent(router.query.timestamp))
11 |       : undefined;
12 | 
13 |   return <TracePage traceId={traceId} timestamp={timestamp} />;
14 | }
15 | 


--------------------------------------------------------------------------------
/web/src/pages/public/traces/[traceId].tsx:
--------------------------------------------------------------------------------
 1 | // This url is deprecated, we keep this redirect page for backward compatibility
 2 | 
 3 | import TraceRedirectPage, {
 4 |   getServerSideProps,
 5 | } from "@/src/pages/trace/[traceId]";
 6 | 
 7 | export { getServerSideProps };
 8 | 
 9 | export default TraceRedirectPage;
10 | 


--------------------------------------------------------------------------------
/web/src/pages/setup.tsx:
--------------------------------------------------------------------------------
1 | import { SetupPage } from "@/src/features/setup/components/SetupPage";
2 | 
3 | export default SetupPage;
4 | 


--------------------------------------------------------------------------------
/web/src/server/api/definitions/evalExecutionsTable.ts:
--------------------------------------------------------------------------------
 1 | import { type ColumnDefinition, JobExecutionStatus } from "@langfuse/shared";
 2 | 
 3 | export const evalExecutionsFilterCols: ColumnDefinition[] = [
 4 |   {
 5 |     name: "Status",
 6 |     id: "status",
 7 |     type: "stringOptions",
 8 |     internal: 'je."status"::text',
 9 |     options: Object.values(JobExecutionStatus)
10 |       .filter((value) => value !== JobExecutionStatus.CANCELLED)
11 |       .map((value) => ({ value })),
12 |   },
13 | ];
14 | 


--------------------------------------------------------------------------------
/web/src/server/api/definitions/usersTable.ts:
--------------------------------------------------------------------------------
 1 | import { type ColumnDefinition } from "@langfuse/shared";
 2 | 
 3 | export const usersTableCols: ColumnDefinition[] = [
 4 |   {
 5 |     name: "Timestamp",
 6 |     id: "timestamp",
 7 |     type: "datetime",
 8 |     internal: 't."timestamp"',
 9 |   },
10 | ];
11 | 


--------------------------------------------------------------------------------
/web/src/server/api/routers/generations/index.ts:
--------------------------------------------------------------------------------
1 | import { createTRPCRouter } from "@/src/server/api/trpc";
2 | import { filterOptionsQuery } from "./filterOptionsQuery";
3 | import { getAllQueries } from "./getAllQueries";
4 | 
5 | export const generationsRouter = createTRPCRouter({
6 |   ...getAllQueries,
7 |   filterOptions: filterOptionsQuery,
8 | });
9 | 


--------------------------------------------------------------------------------
/web/src/server/api/routers/generations/utils/GenerationTableOptions.ts:
--------------------------------------------------------------------------------
 1 | import { z } from "zod/v4";
 2 | import { singleFilter, TracingSearchType } from "@langfuse/shared";
 3 | import { orderBy } from "@langfuse/shared";
 4 | 
 5 | export const GenerationTableOptions = z.object({
 6 |   projectId: z.string(), // Required for protectedProjectProcedure
 7 |   filter: z.array(singleFilter),
 8 |   searchQuery: z.string().nullable(),
 9 |   searchType: z.array(TracingSearchType),
10 |   orderBy: orderBy,
11 | });
12 | 


--------------------------------------------------------------------------------
/web/src/server/utils/checkProjectMembershipOrAdmin.ts:
--------------------------------------------------------------------------------
 1 | import { type User } from "next-auth";
 2 | 
 3 | export const isProjectMemberOrAdmin = (
 4 |   user: User | null | undefined,
 5 |   projectId: string,
 6 | ): boolean => {
 7 |   if (!user) return false;
 8 |   if (user.admin === true) return true;
 9 | 
10 |   const sessionProjects = user.organizations.flatMap((org) => org.projects);
11 |   const isProjectMember = sessionProjects.some(
12 |     (project) => project.id === projectId,
13 |   );
14 | 
15 |   return isProjectMember;
16 | };
17 | 


--------------------------------------------------------------------------------
/web/src/utils/exceptions.ts:
--------------------------------------------------------------------------------
 1 | import { Prisma } from "@langfuse/shared/src/db";
 2 | 
 3 | export function isPrismaException(e: unknown) {
 4 |   return (
 5 |     e instanceof Prisma.PrismaClientKnownRequestError ||
 6 |     e instanceof Prisma.PrismaClientUnknownRequestError ||
 7 |     e instanceof Prisma.PrismaClientRustPanicError ||
 8 |     e instanceof Prisma.PrismaClientInitializationError ||
 9 |     e instanceof Prisma.PrismaClientValidationError
10 |   );
11 | }
12 | 


--------------------------------------------------------------------------------
/web/src/utils/getFinalModelParams.tsx:
--------------------------------------------------------------------------------
 1 | import { type ModelParams, type UIModelParams } from "@langfuse/shared";
 2 | 
 3 | export function getFinalModelParams(modelParams: UIModelParams): ModelParams {
 4 |   return Object.entries(modelParams)
 5 |     .filter(([key, value]) => value.enabled && key !== "maxTemperature")
 6 |     .reduce(
 7 |       (params, [key, value]) => ({ ...params, [key]: value.value }),
 8 |       {} as ModelParams,
 9 |     );
10 | }
11 | 


--------------------------------------------------------------------------------
/web/src/utils/string.ts:
--------------------------------------------------------------------------------
 1 | export function lastCharacters(str: string, n: number) {
 2 |   return str.substring(str.length - n);
 3 | }
 4 | 
 5 | export function truncate(str: string, n: number = 16) {
 6 |   // '...' suffix if the string is longer than n
 7 |   if (str.length > n) {
 8 |     return str.substring(0, n) + "...";
 9 |   }
10 |   return str;
11 | }
12 | 


--------------------------------------------------------------------------------
/web/src/utils/superjson.ts:
--------------------------------------------------------------------------------
 1 | import Decimal from "decimal.js";
 2 | import { registerCustom } from "superjson";
 3 | 
 4 | export const setUpSuperjson = () => {
 5 |   registerCustom<Decimal, string>(
 6 |     {
 7 |       isApplicable: (v): v is Decimal => Decimal.isDecimal(v),
 8 |       serialize: (v) => v.toJSON(),
 9 |       deserialize: (v) => new Decimal(v),
10 |     },
11 |     "decimal.js",
12 |   );
13 | };
14 | 


--------------------------------------------------------------------------------
/web/src/utils/tailwind.ts:
--------------------------------------------------------------------------------
1 | import { clsx, type ClassValue } from "clsx";
2 | import { twMerge } from "tailwind-merge";
3 | 
4 | export function cn(...inputs: ClassValue[]) {
5 |   return twMerge(clsx(inputs));
6 | }
7 | 


--------------------------------------------------------------------------------
/web/tsconfig.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "extends": "@repo/typescript-config/nextjs.json",
 3 |   "compilerOptions": {
 4 |     "declaration": false,
 5 |     "declarationMap": false,
 6 |     "outDir": "dist",
 7 |     "plugins": [
 8 |       {
 9 |         "name": "next"
10 |       }
11 |     ],
12 |     "paths": {
13 |       "@/*": ["./*"]
14 |     },
15 |     "strictNullChecks": true
16 |   },
17 |   "exclude": ["node_modules", "sdk"],
18 |   "include": [
19 |     "src",
20 |     "next-env.d.ts",
21 |     ".next/types/**/*.ts",
22 |     ".eslintrc.js",
23 |     "next-env.d.ts",
24 |     "**/*.ts",
25 |     "**/*.tsx",
26 |     "**/*.cjs",
27 |     "**/*.mjs",
28 |     "types/global.d.ts"
29 |   ]
30 | }
31 | 


--------------------------------------------------------------------------------
/web/types/global.d.ts:
--------------------------------------------------------------------------------
1 | declare namespace JSX {
2 |   interface IntrinsicElements {
3 |     "stripe-pricing-table": React.DetailedHTMLProps<
4 |       React.HTMLAttributes<HTMLElement>,
5 |       HTMLElement
6 |     >;
7 |   }
8 | }
9 | 


--------------------------------------------------------------------------------
/worker/.eslintrc.js:
--------------------------------------------------------------------------------
 1 | /** @type {import("eslint").Linter.Config} */
 2 | module.exports = {
 3 |   extends: ["@repo/eslint-config/library.js"],
 4 |   parser: "@typescript-eslint/parser",
 5 |   parserOptions: {
 6 |     project: true,
 7 |   },
 8 |   ignorePatterns: ["**/*test*.*"],
 9 | };
10 | 


--------------------------------------------------------------------------------
/worker/src/backgroundMigrations/IBackgroundMigration.ts:
--------------------------------------------------------------------------------
1 | export interface IBackgroundMigration {
2 |   validate: (
3 |     args: Record<string, unknown>,
4 |   ) => Promise<{ valid: boolean; invalidReason: string | undefined }>;
5 |   run: (args: Record<string, unknown>) => Promise<void>;
6 |   abort: () => Promise<void>;
7 | }
8 | 


--------------------------------------------------------------------------------
/worker/src/constants/VERSION.ts:
--------------------------------------------------------------------------------
1 | export const VERSION = "v3.68.0";
2 | 


--------------------------------------------------------------------------------
/worker/src/database.ts:
--------------------------------------------------------------------------------
 1 | import { Kysely, PostgresDialect } from "kysely";
 2 | import { Pool } from "pg";
 3 | import { DB } from "@langfuse/shared";
 4 | import { env } from "./env";
 5 | 
 6 | export const db = new Kysely<DB>({
 7 |   dialect: new PostgresDialect({
 8 |     pool: new Pool({
 9 |       connectionString: env.DATABASE_URL,
10 |     }),
11 |   }),
12 | });
13 | 


--------------------------------------------------------------------------------
/worker/src/ee/cloudUsageMetering/constants.ts:
--------------------------------------------------------------------------------
1 | export const cloudUsageMeteringDbCronJobName = "cloud_usage_metering";
2 | 
3 | export enum CloudUsageMeteringDbCronJobStates {
4 |   Queued = "queued",
5 |   Processing = "processing",
6 | }
7 | 


--------------------------------------------------------------------------------
/worker/src/index.ts:
--------------------------------------------------------------------------------
1 | import "./instrumentation"; // instrumenting the application
2 | import app from "./app";
3 | import { env } from "./env";
4 | import { logger } from "@langfuse/shared/src/server";
5 | 
6 | export const server = app.listen(env.PORT, env.HOSTNAME, () => {
7 |   logger.info(`Listening: http://${env.HOSTNAME}:${env.PORT}`);
8 | });
9 | 


--------------------------------------------------------------------------------
/worker/src/initialize.ts:
--------------------------------------------------------------------------------
1 | import { upsertDefaultModelPrices } from "./scripts/upsertDefaultModelPrices";
2 | import { upsertManagedEvaluators } from "./scripts/upsertManagedEvaluators";
3 | import { upsertLangfuseDashboards } from "./scripts/upsertLangfuseDashboards";
4 | 
5 | upsertDefaultModelPrices();
6 | upsertManagedEvaluators();
7 | upsertLangfuseDashboards();
8 | 


--------------------------------------------------------------------------------
/worker/src/interfaces/ErrorResponse.ts:
--------------------------------------------------------------------------------
1 | import MessageResponse from "./MessageResponse";
2 | 
3 | export default interface ErrorResponse extends MessageResponse {
4 |   stack?: string;
5 | }
6 | 


--------------------------------------------------------------------------------
/worker/src/interfaces/MessageResponse.ts:
--------------------------------------------------------------------------------
1 | export default interface MessageResponse {
2 |   message: string;
3 | }
4 | 


--------------------------------------------------------------------------------
/worker/src/queues/scoreDelete.ts:
--------------------------------------------------------------------------------
 1 | import { Job, Processor } from "bullmq";
 2 | import { QueueName, TQueueJobTypes } from "@langfuse/shared/src/server";
 3 | 
 4 | import { processClickhouseScoreDelete } from "../features/scores/processClickhouseScoreDelete";
 5 | 
 6 | export const scoreDeleteProcessor: Processor = async (
 7 |   job: Job<TQueueJobTypes[QueueName.ScoreDelete]>,
 8 | ): Promise<void> => {
 9 |   const { scoreIds, projectId } = job.data.payload;
10 |   await processClickhouseScoreDelete(projectId, scoreIds);
11 | };
12 | 


--------------------------------------------------------------------------------
/worker/tsconfig.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "extends": "@repo/typescript-config/base.json",
 3 |   "compilerOptions": {
 4 |     "esModuleInterop": true,
 5 |     "module": "Node16",
 6 |     "moduleResolution": "Node16",
 7 |     "declaration": false,
 8 |     "declarationMap": false,
 9 |     "lib": ["ES2021"],
10 |     "outDir": "./dist",
11 |     "types": ["node"],
12 |     "downlevelIteration": true,
13 |     "resolveJsonModule": true
14 |   },
15 |   "include": ["."],
16 |   "exclude": ["node_modules", "dist", "src/**/*.test.ts"]
17 | }
18 | 


--------------------------------------------------------------------------------├── .codespellrc
├── .cursor
    ├── Dockerfile
    ├── environment.json
    └── rules
    │   ├── authorization-and-rbac.mdc
    │   ├── entitlements.mdc
    │   ├── frontend-features.mdc
    │   ├── general-info.mdc
    │   └── public-api.mdc
├── .dockerignore
├── .env.dev-azure.example
├── .env.dev.example
├── .env.prod.example
├── .eslintignore
├── .github
    ├── CODEOWNERS
    ├── DISCUSSION_TEMPLATE
    │   └── ideas.yml
    ├── ISSUE_TEMPLATE
    │   ├── bug_report.yml
    │   └── config.yml
    ├── PULL_REQUEST_TEMPLATE.md
    ├── dependabot.yml
    └── workflows
    │   ├── _deploy_ecs_service.yml
    │   ├── ci.yml.template
    │   ├── codeql.yml
    │   ├── codespell.yml
    │   ├── dependabot-rebase-stale.yml
    │   ├── deploy.yml
    │   ├── licencecheck.yml
    │   ├── pipeline.yml
    │   ├── release.yml
    │   ├── snyk.yml
    │   └── stale_issues.yml
├── .gitignore
├── .husky
    ├── pre-commit
    └── pre-push
├── .npmrc
├── .nvmrc
├── .vscode
    ├── extensions.json
    ├── launch.json
    └── settings.json
├── AGENTS.md
├── CONTRIBUTING.md
├── LICENSE
├── README.cn.md
├── README.ja.md
├── README.kr.md
├── README.md
├── SECURITY.md
├── docker-compose.build.yml
├── docker-compose.dev-azure.yml
├── docker-compose.dev.yml
├── docker-compose.yml
├── ee
    ├── .eslintrc.js
    ├── LICENSE
    ├── README.md
    ├── package.json
    ├── src
    │   ├── ee-license-check
    │   │   └── index.ts
    │   ├── env.ts
    │   └── index.ts
    └── tsconfig.json
├── fern
    ├── apis
    │   ├── client
    │   │   ├── definition
    │   │   │   ├── api.yml
    │   │   │   ├── commons.yml
    │   │   │   └── score.yml
    │   │   └── generators.yml
    │   ├── organizations
    │   │   ├── definition
    │   │   │   ├── api.yml
    │   │   │   ├── commons.yml
    │   │   │   └── organizations.yml
    │   │   └── generators.yml
    │   └── server
    │   │   ├── definition
    │   │       ├── annotation-queues.yml
    │   │       ├── api.yml
    │   │       ├── comments.yml
    │   │       ├── commons.yml
    │   │       ├── dataset-items.yml
    │   │       ├── dataset-run-items.yml
    │   │       ├── datasets.yml
    │   │       ├── health.yml
    │   │       ├── ingestion.yml
    │   │       ├── media.yml
    │   │       ├── metrics.yml
    │   │       ├── models.yml
    │   │       ├── observations.yml
    │   │       ├── organizations.yml
    │   │       ├── projects.yml
    │   │       ├── prompt-version.yml
    │   │       ├── prompts.yml
    │   │       ├── scim.yml
    │   │       ├── score-configs.yml
    │   │       ├── score-v2.yml
    │   │       ├── score.yml
    │   │       ├── sessions.yml
    │   │       ├── trace.yml
    │   │       └── utils
    │   │       │   └── pagination.yml
    │   │   └── generators.yml
    └── fern.config.json
├── generated
    └── .gitignore
├── package.json
├── packages
    ├── config-eslint
    │   ├── library.js
    │   ├── next.js
    │   └── package.json
    ├── config-typescript
    │   ├── base.json
    │   ├── nextjs.json
    │   └── package.json
    └── shared
    │   ├── .eslintrc.js
    │   ├── clickhouse
    │       ├── migrations
    │       │   ├── clustered
    │       │   │   ├── 0001_traces.down.sql
    │       │   │   ├── 0001_traces.up.sql
    │       │   │   ├── 0002_observations.down.sql
    │       │   │   ├── 0002_observations.up.sql
    │       │   │   ├── 0003_scores.down.sql
    │       │   │   ├── 0003_scores.up.sql
    │       │   │   ├── 0004_drop_observations_index.down.sql
    │       │   │   ├── 0004_drop_observations_index.up.sql
    │       │   │   ├── 0005_add_session_id_index.down.sql
    │       │   │   ├── 0005_add_session_id_index.up.sql
    │       │   │   ├── 0006_add_user_id_index.down.sql
    │       │   │   ├── 0006_add_user_id_index.up.sql
    │       │   │   ├── 0007_add_event_log.down.sql
    │       │   │   ├── 0007_add_event_log.up.sql
    │       │   │   ├── 0008_add_environments_column.down.sql
    │       │   │   ├── 0008_add_environments_column.up.sql
    │       │   │   ├── 0009_add_project_environments.down.sql
    │       │   │   ├── 0009_add_project_environments.up.sql
    │       │   │   ├── 0010_add_metadata_column_on_scores.down.sql
    │       │   │   ├── 0010_add_metadata_column_on_scores.up.sql
    │       │   │   ├── 0011_add_blob_storage_file_log.down.sql
    │       │   │   ├── 0011_add_blob_storage_file_log.up.sql
    │       │   │   ├── 0012_add_session_id_column_scores.down.sql
    │       │   │   ├── 0012_add_session_id_column_scores.up.sql
    │       │   │   ├── 0013_drop_scores_trace_id_index.down.sql
    │       │   │   ├── 0013_drop_scores_trace_id_index.up.sql
    │       │   │   ├── 0014_scores_modify_nullable_trace_id_column.down.sql
    │       │   │   ├── 0014_scores_modify_nullable_trace_id_column.up.sql
    │       │   │   ├── 0015_add_scores_trace_index.down.sql
    │       │   │   ├── 0015_add_scores_trace_index.up.sql
    │       │   │   ├── 0016_add_scores_session_index.down.sql
    │       │   │   ├── 0016_add_scores_session_index.up.sql
    │       │   │   ├── 0017_add_run_id_column_scores.down.sql
    │       │   │   ├── 0017_add_run_id_column_scores.up.sql
    │       │   │   ├── 0018_add_scores_run_index.down.sql
    │       │   │   ├── 0018_add_scores_run_index.up.sql
    │       │   │   ├── 0019_analytics_traces.down.sql
    │       │   │   ├── 0019_analytics_traces.up.sql
    │       │   │   ├── 0020_analytics_observations.down.sql
    │       │   │   ├── 0020_analytics_observations.up.sql
    │       │   │   ├── 0021_analytics_scores.down.sql
    │       │   │   └── 0021_analytics_scores.up.sql
    │       │   └── unclustered
    │       │   │   ├── 0001_traces.down.sql
    │       │   │   ├── 0001_traces.up.sql
    │       │   │   ├── 0002_observations.down.sql
    │       │   │   ├── 0002_observations.up.sql
    │       │   │   ├── 0003_scores.down.sql
    │       │   │   ├── 0003_scores.up.sql
    │       │   │   ├── 0004_drop_observations_index.down.sql
    │       │   │   ├── 0004_drop_observations_index.up.sql
    │       │   │   ├── 0005_add_session_id_index.down.sql
    │       │   │   ├── 0005_add_session_id_index.up.sql
    │       │   │   ├── 0006_add_user_id_index.down.sql
    │       │   │   ├── 0006_add_user_id_index.up.sql
    │       │   │   ├── 0007_add_event_log.down.sql
    │       │   │   ├── 0007_add_event_log.up.sql
    │       │   │   ├── 0008_add_environments_column.down.sql
    │       │   │   ├── 0008_add_environments_column.up.sql
    │       │   │   ├── 0009_add_project_environments.down.sql
    │       │   │   ├── 0009_add_project_environments.up.sql
    │       │   │   ├── 0010_add_metadata_column_on_scores.down.sql
    │       │   │   ├── 0010_add_metadata_column_on_scores.up.sql
    │       │   │   ├── 0011_add_blob_storage_file_log.down.sql
    │       │   │   ├── 0011_add_blob_storage_file_log.up.sql
    │       │   │   ├── 0012_add_session_id_column_scores.down.sql
    │       │   │   ├── 0012_add_session_id_column_scores.up.sql
    │       │   │   ├── 0013_drop_scores_trace_id_index.down.sql
    │       │   │   ├── 0013_drop_scores_trace_id_index.up.sql
    │       │   │   ├── 0014_scores_modify_nullable_trace_id_column.down.sql
    │       │   │   ├── 0014_scores_modify_nullable_trace_id_column.up.sql
    │       │   │   ├── 0015_add_scores_trace_index.down.sql
    │       │   │   ├── 0015_add_scores_trace_index.up.sql
    │       │   │   ├── 0016_add_scores_session_index.down.sql
    │       │   │   ├── 0016_add_scores_session_index.up.sql
    │       │   │   ├── 0017_add_run_id_column_scores.down.sql
    │       │   │   ├── 0017_add_run_id_column_scores.up.sql
    │       │   │   ├── 0018_add_scores_run_index.down.sql
    │       │   │   ├── 0018_add_scores_run_index.up.sql
    │       │   │   ├── 0019_analytics_traces.down.sql
    │       │   │   ├── 0019_analytics_traces.up.sql
    │       │   │   ├── 0020_analytics_observations.down.sql
    │       │   │   ├── 0020_analytics_observations.up.sql
    │       │   │   ├── 0021_analytics_scores.down.sql
    │       │   │   └── 0021_analytics_scores.up.sql
    │       └── scripts
    │       │   ├── down.sh
    │       │   ├── drop.sh
    │       │   ├── seed.ts
    │       │   └── up.sh
    │   ├── package.json
    │   ├── prisma
    │       ├── database.svg
    │       ├── generated
    │       │   └── types.ts
    │       ├── migrations
    │       │   ├── 20230518191501_init
    │       │   │   └── migration.sql
    │       │   ├── 20230518193415_add_observaionts_and_traces
    │       │   │   └── migration.sql
    │       │   ├── 20230518193521_changes
    │       │   │   └── migration.sql
    │       │   ├── 20230522092340_add_metrics_and_observation_types
    │       │   │   └── migration.sql
    │       │   ├── 20230522094431_endtime_optional
    │       │   │   └── migration.sql
    │       │   ├── 20230522131516_default_timestamp
    │       │   │   └── migration.sql
    │       │   ├── 20230523082455_rename_metrics_to_gradings
    │       │   │   └── migration.sql
    │       │   ├── 20230523084523_rename_to_score
    │       │   │   └── migration.sql
    │       │   ├── 20230529140133_user_add_pw
    │       │   │   └── migration.sql
    │       │   ├── 20230530204241_auth_api_ui
    │       │   │   └── migration.sql
    │       │   ├── 20230618125818_remove_status_from_trace
    │       │   │   └── migration.sql
    │       │   ├── 20230620181114_restructure
    │       │   │   └── migration.sql
    │       │   ├── 20230622114254_new_oservations
    │       │   │   └── migration.sql
    │       │   ├── 20230623172401_observation_add_level_and_status_message
    │       │   │   └── migration.sql
    │       │   ├── 20230626095337_external_trace_id
    │       │   │   └── migration.sql
    │       │   ├── 20230705160335_add_created_updated_timestamps
    │       │   │   └── migration.sql
    │       │   ├── 20230706195819_add_completion_start_time
    │       │   │   └── migration.sql
    │       │   ├── 20230707132314_traces_project_id_index
    │       │   │   └── migration.sql
    │       │   ├── 20230707133415_user_add_email_index
    │       │   │   └── migration.sql
    │       │   ├── 20230710105741_added_indices
    │       │   │   └── migration.sql
    │       │   ├── 20230710114928_traces_add_user_id
    │       │   │   └── migration.sql
    │       │   ├── 20230710200816_scores_add_comment
    │       │   │   └── migration.sql
    │       │   ├── 20230711104810_traces_add_index
    │       │   │   └── migration.sql
    │       │   ├── 20230711110517_memberships_add_userid_index
    │       │   │   └── migration.sql
    │       │   ├── 20230711112235_fix_indices
    │       │   │   └── migration.sql
    │       │   ├── 20230717190411_users_feature_flags
    │       │   │   └── migration.sql
    │       │   ├── 20230720162550_tokens
    │       │   │   └── migration.sql
    │       │   ├── 20230720164603_migrate_tokens
    │       │   │   └── migration.sql
    │       │   ├── 20230720172051_tokens_non_null
    │       │   │   └── migration.sql
    │       │   ├── 20230721111651_drop_usage_json
    │       │   │   └── migration.sql
    │       │   ├── 20230731162154_score_value_float
    │       │   │   └── migration.sql
    │       │   ├── 20230803093326_add_release_and_version
    │       │   │   └── migration.sql
    │       │   ├── 20230809093636_remove_foreign_keys
    │       │   │   └── migration.sql
    │       │   ├── 20230809132331_add_project_id_to_observations
    │       │   │   └── migration.sql
    │       │   ├── 20230810191452_traceid_nullable_on_observations
    │       │   │   └── migration.sql
    │       │   ├── 20230810191453_project_id_not_null
    │       │   │   └── migration.sql
    │       │   ├── 20230814184705_add_viewer_membership_role
    │       │   │   └── migration.sql
    │       │   ├── 20230901155252_add_pricings_table
    │       │   │   └── migration.sql
    │       │   ├── 20230901155336_add_pricing_data
    │       │   │   └── migration.sql
    │       │   ├── 20230907204921_add_cron_jobs_table
    │       │   │   └── migration.sql
    │       │   ├── 20230907225603_projects_updated_at
    │       │   │   └── migration.sql
    │       │   ├── 20230907225604_api_keys_publishable_to_public
    │       │   │   └── migration.sql
    │       │   ├── 20230910164603_cron_add_state
    │       │   │   └── migration.sql
    │       │   ├── 20230912115644_add_trace_public_bool
    │       │   │   └── migration.sql
    │       │   ├── 20230918180320_add_indices
    │       │   │   └── migration.sql
    │       │   ├── 20230922030325_add_observation_index
    │       │   │   └── migration.sql
    │       │   ├── 20230924232619_datasets_init
    │       │   │   └── migration.sql
    │       │   ├── 20230924232620_datasets_continued
    │       │   │   └── migration.sql
    │       │   ├── 20231004005909_add_parent_observation_id_index
    │       │   │   └── migration.sql
    │       │   ├── 20231005064433_add_release_index
    │       │   │   └── migration.sql
    │       │   ├── 20231009095917_add_ondelete_cascade
    │       │   │   └── migration.sql
    │       │   ├── 20231012161041_add_events_table
    │       │   │   └── migration.sql
    │       │   ├── 20231014131841_users_add_admin_flag
    │       │   │   └── migration.sql
    │       │   ├── 20231018130032_add_per_1000_chars_pricing
    │       │   │   └── migration.sql
    │       │   ├── 20231019094815_add_additional_secret_key_column
    │       │   │   └── migration.sql
    │       │   ├── 20231021182825_user_emails_all_lowercase
    │       │   │   └── migration.sql
    │       │   ├── 20231025153548_add_headers_to_events
    │       │   │   └── migration.sql
    │       │   ├── 20231030184329_events_add_index_on_projectid
    │       │   │   └── migration.sql
    │       │   ├── 20231104004529_scores_add_index
    │       │   │   └── migration.sql
    │       │   ├── 20231104005403_fkey_indicies
    │       │   │   └── migration.sql
    │       │   ├── 20231106213824_add_openai_models
    │       │   │   └── migration.sql
    │       │   ├── 20231110012457_observation_created_at
    │       │   │   └── migration.sql
    │       │   ├── 20231110012829_observation_created_at_index
    │       │   │   └── migration.sql
    │       │   ├── 20231112095703_observations_add_unique_constraint
    │       │   │   └── migration.sql
    │       │   ├── 20231116005353_scores_unique_id_projectid
    │       │   │   └── migration.sql
    │       │   ├── 20231119171939_cron_add_job_started_at
    │       │   │   └── migration.sql
    │       │   ├── 20231119171940_bookmarked
    │       │   │   └── migration.sql
    │       │   ├── 20231129013314_invites
    │       │   │   └── migration.sql
    │       │   ├── 20231130003317_trace_session_input_output
    │       │   │   └── migration.sql
    │       │   ├── 20231204223505_add_unit_to_observations
    │       │   │   └── migration.sql
    │       │   ├── 20231223230007_cloud_config
    │       │   │   └── migration.sql
    │       │   ├── 20231223230008_accounts_add_cols_azure_ad_auth
    │       │   │   └── migration.sql
    │       │   ├── 20231230151856_add_prompt_table
    │       │   │   └── migration.sql
    │       │   ├── 20240103135918_add_pricings
    │       │   │   └── migration.sql
    │       │   ├── 20240104210051_add_model_indices
    │       │   │   └── migration.sql
    │       │   ├── 20240104210052_add_model_indices_pricing
    │       │   │   └── migration.sql
    │       │   ├── 20240105010215_add_tags_in_traces
    │       │   │   └── migration.sql
    │       │   ├── 20240105170551_index_tags_in_traces
    │       │   │   └── migration.sql
    │       │   ├── 20240106195340_drop_dataset_status
    │       │   │   └── migration.sql
    │       │   ├── 20240111152124_add_gpt_35_pricing
    │       │   │   └── migration.sql
    │       │   ├── 20240117151938_traces_remove_unique_id_external
    │       │   │   └── migration.sql
    │       │   ├── 20240117165747_add_cost_to_observations
    │       │   │   └── migration.sql
    │       │   ├── 20240118204639_add_models_table
    │       │   │   └── migration.sql
    │       │   ├── 20240118204936_add_internal_model
    │       │   │   └── migration.sql
    │       │   ├── 20240118204937_add_observations_view
    │       │   │   └── migration.sql
    │       │   ├── 20240118235424_add_index_to_models
    │       │   │   └── migration.sql
    │       │   ├── 20240119140941_add_tokenizer_id
    │       │   │   └── migration.sql
    │       │   ├── 20240119164147_make_model_params_nullable
    │       │   │   └── migration.sql
    │       │   ├── 20240119164148_add_models
    │       │   │   └── migration.sql
    │       │   ├── 20240124140443_session_composite_key
    │       │   │   └── migration.sql
    │       │   ├── 20240124164148_correct_models
    │       │   │   └── migration.sql
    │       │   ├── 20240126184148_new_models copy
    │       │   │   └── migration.sql
    │       │   ├── 20240130100110_usage_unit_nullable
    │       │   │   └── migration.sql
    │       │   ├── 20240130160110_claude_models
    │       │   │   └── migration.sql
    │       │   ├── 20240131184148_add_finetuned_and_vertex_models
    │       │   │   └── migration.sql
    │       │   ├── 20240203184148_update_pricing
    │       │   │   └── migration.sql
    │       │   ├── 20240212175433_add_audit_log_table
    │       │   │   └── migration.sql
    │       │   ├── 20240213124148_update_openai_pricing
    │       │   │   └── migration.sql
    │       │   ├── 20240214232619_prompts_add_indicies
    │       │   │   └── migration.sql
    │       │   ├── 20240215224148_update_openai_pricing
    │       │   │   └── migration.sql
    │       │   ├── 20240215234937_fix_observations_view
    │       │   │   └── migration.sql
    │       │   ├── 20240219162415_add_prompt_config
    │       │   │   └── migration.sql
    │       │   ├── 20240226165118_add_observations_index
    │       │   │   └── migration.sql
    │       │   ├── 20240226182815_add_model_index
    │       │   │   └── migration.sql
    │       │   ├── 20240226183642_add_observations_index
    │       │   │   └── migration.sql
    │       │   ├── 20240226202040_add_observations_trace_id_project_id_start_time_idx
    │       │   │   └── migration.sql
    │       │   ├── 20240226202041_add_observations_trace_id_project_id_type_start_time_idx
    │       │   │   └── migration.sql
    │       │   ├── 20240226203642_rewrite_observations_view
    │       │   │   └── migration.sql
    │       │   ├── 20240227112101_index_prompt_id_in_observations
    │       │   │   └── migration.sql
    │       │   ├── 20240228103642_observations_view_cte
    │       │   │   └── migration.sql
    │       │   ├── 20240228123642_observations_view_fix
    │       │   │   └── migration.sql
    │       │   ├── 20240304123642_traces_view
    │       │   │   └── migration.sql
    │       │   ├── 20240304123642_traces_view_improvement
    │       │   │   └── migration.sql
    │       │   ├── 20240304222519_scores_add_index
    │       │   │   └── migration.sql
    │       │   ├── 20240305095119_add_observations_index
    │       │   │   └── migration.sql
    │       │   ├── 20240305100713_traces_add_index
    │       │   │   └── migration.sql
    │       │   ├── 20240307090110_claude_model_three
    │       │   │   └── migration.sql
    │       │   ├── 20240307185543_score_add_source_nullable
    │       │   │   └── migration.sql
    │       │   ├── 20240307185544_score_add_name_index
    │       │   │   └── migration.sql
    │       │   ├── 20240307185725_backfill_score_source
    │       │   │   └── migration.sql
    │       │   ├── 20240312195727_score_source_drop_default
    │       │   │   └── migration.sql
    │       │   ├── 20240314090110_claude_model
    │       │   │   └── migration.sql
    │       │   ├── 20240325211959_remove_example_table
    │       │   │   └── migration.sql
    │       │   ├── 20240325212245_dataset_runs_add_metadata
    │       │   │   └── migration.sql
    │       │   ├── 20240326114211_dataset_run_item_bind_to_trace
    │       │   │   └── migration.sql
    │       │   ├── 20240326114337_dataset_run_item_backfill_trace_id
    │       │   │   └── migration.sql
    │       │   ├── 20240326115136_dataset_run_item_traceid_non_null
    │       │   │   └── migration.sql
    │       │   ├── 20240326115424_dataset_run_item_index_trace
    │       │   │   └── migration.sql
    │       │   ├── 20240328065738_dataset_item_input_nullable
    │       │   │   └── migration.sql
    │       │   ├── 20240404203640_dataset_item_source_trace_id
    │       │   │   └── migration.sql
    │       │   ├── 20240404210315_dataset_add_descriptions
    │       │   │   └── migration.sql
    │       │   ├── 20240404232317_dataset_items_backfill_source_trace_id
    │       │   │   └── migration.sql
    │       │   ├── 20240405124810_prompt_to_json
    │       │   │   └── migration.sql
    │       │   ├── 20240408133037_add_objects_for_evals
    │       │   │   └── migration.sql
    │       │   ├── 20240408134328_prompt_table_add_tags
    │       │   │   └── migration.sql
    │       │   ├── 20240408134330_prompt_table_add_index_to_tags
    │       │   │   └── migration.sql
    │       │   ├── 20240411134330_model_updates
    │       │   │   └── migration.sql
    │       │   ├── 20240411194142_update_job_config_status
    │       │   │   └── migration.sql
    │       │   ├── 20240411224142_update_models
    │       │   │   └── migration.sql
    │       │   ├── 20240414203636_ee_add_sso_configs
    │       │   │   └── migration.sql
    │       │   ├── 20240415235737_index_models_model_name
    │       │   │   └── migration.sql
    │       │   ├── 20240416173813_add_internal_model_index
    │       │   │   └── migration.sql
    │       │   ├── 20240417102742_metadata_on_dataset_and_dataset_item
    │       │   │   └── migration.sql
    │       │   ├── 20240419152924_posthog_integration_settings
    │       │   │   └── migration.sql
    │       │   ├── 20240420134232_posthog_integration_created_at
    │       │   │   └── migration.sql
    │       │   ├── 20240423174013_update_models
    │       │   │   └── migration.sql
    │       │   ├── 20240423192655_add_llm_api_keys
    │       │   │   └── migration.sql
    │       │   ├── 20240424150909_add_job_execution_index
    │       │   │   └── migration.sql
    │       │   ├── 20240429124411_add_prompt_version_labels
    │       │   │   └── migration.sql
    │       │   ├── 20240429194411_add_latest_prompt_tag
    │       │   │   └── migration.sql
    │       │   ├── 20240503125742_traces_add_createdat_updatedat
    │       │   │   └── migration.sql
    │       │   ├── 20240503130335_traces_index_created_at
    │       │   │   └── migration.sql
    │       │   ├── 20240503130520_traces_index_updated_at
    │       │   │   └── migration.sql
    │       │   ├── 20240508132621_scores_add_project_id
    │       │   │   └── migration.sql
    │       │   ├── 20240508132735_scores_add_projectid_index
    │       │   │   └── migration.sql
    │       │   ├── 20240508132736_scores_backfill_project_id
    │       │   │   └── migration.sql
    │       │   ├── 20240512151529_rename_memberships_to_project_memberships
    │       │   │   └── migration.sql
    │       │   ├── 20240512155020_rename_enum_membership_role_to_project_role
    │       │   │   └── migration.sql
    │       │   ├── 20240512155021_add_pricing_gpt4o
    │       │   │   └── migration.sql
    │       │   ├── 20240512155021_scores_drop_fk_on_traces_and_observations
    │       │   │   └── migration.sql
    │       │   ├── 20240512155022_scores_non_null_and_add_fk_project_id
    │       │   │   └── migration.sql
    │       │   ├── 20240513082203_scores_unique_id_and_projectid_instead_of_id_and_traceid
    │       │   │   └── migration.sql
    │       │   ├── 20240513082204_scores_unique_id_and_projectid_instead_of_id_and_traceid_index
    │       │   │   └── migration.sql
    │       │   ├── 20240513082205_observations_view_add_time_to_first_token
    │       │   │   └── migration.sql
    │       │   ├── 20240522081254_scores_add_author_user_id
    │       │   │   └── migration.sql
    │       │   ├── 20240522095738_scores_add_author_user_id_index
    │       │   │   └── migration.sql
    │       │   ├── 20240523142425_score_config_add_table
    │       │   │   └── migration.sql
    │       │   ├── 20240523142524_scores_add_config_id_idx
    │       │   │   └── migration.sql
    │       │   ├── 20240523142610_scores_add_fk_scores_config_id
    │       │   │   └── migration.sql
    │       │   ├── 20240524154058_scores_source_enum_add_annotation
    │       │   │   └── migration.sql
    │       │   ├── 20240524156058_scores_source_backfill_annotation_for_review
    │       │   │   └── migration.sql
    │       │   ├── 20240524165931_scores_source_enum_drop_review
    │       │   │   └── migration.sql
    │       │   ├── 20240524190433_job_executions_add_fk_index_config_id
    │       │   │   └── migration.sql
    │       │   ├── 20240524190434_job_executions_add_fk_index_score_id
    │       │   │   └── migration.sql
    │       │   ├── 20240524190435_job_executions_add_fk_index_trace_id
    │       │   │   └── migration.sql
    │       │   ├── 20240524190436_job_executions_index_created_at
    │       │   │   └── migration.sql
    │       │   ├── 20240528214726_add_cursor_new_columns_observations
    │       │   │   └── migration.sql
    │       │   ├── 20240528214727_add_cursor_new_columns_scores
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_01
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_02
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_03
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_04
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_05
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_06
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_07
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_08
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_09
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_10
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_11
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_12
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_13
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_14
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_15
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_16
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_17
    │       │   │   └── migration.sql
    │       │   ├── 20240528214728_add_cursor_index_18
    │       │   │   └── migration.sql
    │       │   ├── 20240603212024_dataset_items_add_index_source_trace_id
    │       │   │   └── migration.sql
    │       │   ├── 20240604133338_scores_add_index_name
    │       │   │   └── migration.sql
    │       │   ├── 20240604133339_score_data_type_add_boolean
    │       │   │   └── migration.sql
    │       │   ├── 20240606093356_drop_unused_pricings_table
    │       │   │   └── migration.sql
    │       │   ├── 20240606133011_remove_trace_fkey_datasetrunitems
    │       │   │   └── migration.sql
    │       │   ├── 20240607090858_pricings_add_latest_gemini_models
    │       │   │   └── migration.sql
    │       │   ├── 20240607212419_model_price_anthropic_via_google_vertex
    │       │   │   └── migration.sql
    │       │   ├── 20240611105521_llm_api_keys_custom_endpoints
    │       │   │   └── migration.sql
    │       │   ├── 20240611113517_backfill_manual_score_configs
    │       │   │   └── migration.sql
    │       │   ├── 20240612101858_add_index_observations_project_id_prompt_id
    │       │   │   └── migration.sql
    │       │   ├── 20240617094803_observations_remove_prompt_fk_constraint
    │       │   │   └── migration.sql
    │       │   ├── 20240618134129_add_batch_exports_table
    │       │   │   └── migration.sql
    │       │   ├── 20240618164950_drop_observations_parent_observation_id_idx
    │       │   │   └── migration.sql
    │       │   ├── 20240618164951_drop_observations_updated_at_idx
    │       │   │   └── migration.sql
    │       │   ├── 20240618164952_drop_scores_updated_at_idx
    │       │   │   └── migration.sql
    │       │   ├── 20240618164953_drop_traces_external_id_idx
    │       │   │   └── migration.sql
    │       │   ├── 20240618164954_drop_traces_release_idx
    │       │   │   └── migration.sql
    │       │   ├── 20240618164955_drop_traces_updated_at_idx
    │       │   │   └── migration.sql
    │       │   ├── 20240618164956_create_traces_project_id_timestamp_idx
    │       │   │   └── migration.sql
    │       │   ├── 20240624133412_models_add_anthropic_3_5_sonnet
    │       │   │   └── migration.sql
    │       │   ├── 20240625103957_observations_add_calculated_cost_columns
    │       │   │   └── migration.sql
    │       │   ├── 20240625103958_fix_model_match_gpt4_vision
    │       │   │   └── migration.sql
    │       │   ├── 20240703214747_models_anthropic_aws_bedrock
    │       │   │   └── migration.sql
    │       │   ├── 20240704103900_observations_view_read_from_calculated
    │       │   │   └── migration.sql
    │       │   ├── 20240704103901_scores_make_value_optional
    │       │   │   └── migration.sql
    │       │   ├── 20240705152639_traces_view_add_created_at_updated_at
    │       │   │   └── migration.sql
    │       │   ├── 20240705154048_observation_view_add_created_at_updated_at
    │       │   │   └── migration.sql
    │       │   ├── 20240710114043_score_configs_drop_empty_categories_array_for_numeric_scores
    │       │   │   └── migration.sql
    │       │   ├── 20240710114044_add_pricing_gpt4o_mini
    │       │   │   └── migration.sql
    │       │   ├── 20240718004923_datasets_tables_add_projectid_composite_key
    │       │   │   └── migration.sql
    │       │   ├── 20240718011733_dataset_runs_add_unique_dataset_id_project_id_name copy
    │       │   │   └── migration.sql
    │       │   ├── 20240718011734_dataset_runs_drop_unique_dataset_id_name
    │       │   │   └── migration.sql
    │       │   ├── 20240718011735_observation_view_add_prompt_name_and_version
    │       │   │   └── migration.sql
    │       │   ├── 20240807111358_models_add_openai_gpt_4o_2024_08_06
    │       │   │   └── migration.sql
    │       │   ├── 20240807111359_add_organizations_main_migration
    │       │   │   └── migration.sql
    │       │   ├── 20240814223824_model_fix_text_embedding_3_large
    │       │   │   └── migration.sql
    │       │   ├── 20240814233029_dataset_items_drop_fkey_on_traces_and_observations
    │       │   │   └── migration.sql
    │       │   ├── 20240815171916_add_comments
    │       │   │   └── migration.sql
    │       │   ├── 20240913095558_models_add_openai_o1_2024-09-12
    │       │   │   └── migration.sql
    │       │   ├── 20240913185822_account_add_refresh_token_expires_in
    │       │   │   └── migration.sql
    │       │   ├── 20240917183001_remove_covered_indexes_01
    │       │   │   └── migration.sql
    │       │   ├── 20240917183002_remove_covered_indexes_02
    │       │   │   └── migration.sql
    │       │   ├── 20240917183003_remove_covered_indexes_03
    │       │   │   └── migration.sql
    │       │   ├── 20240917183004_remove_covered_indexes_04
    │       │   │   └── migration.sql
    │       │   ├── 20240917183005_remove_covered_indexes_05
    │       │   │   └── migration.sql
    │       │   ├── 20240917183006_remove_covered_indexes_06
    │       │   │   └── migration.sql
    │       │   ├── 20240917183007_remove_covered_indexes_07
    │       │   │   └── migration.sql
    │       │   ├── 20240917183008_remove_covered_indexes_08
    │       │   │   └── migration.sql
    │       │   ├── 20240917183009_remove_covered_indexes_09
    │       │   │   └── migration.sql
    │       │   ├── 20240917183010_remove_covered_indexes_10
    │       │   │   └── migration.sql
    │       │   ├── 20240917183011_remove_covered_indexes_11
    │       │   │   └── migration.sql
    │       │   ├── 20240917183012_remove_covered_indexes_12
    │       │   │   └── migration.sql
    │       │   ├── 20240917183013_remove_covered_indexes_13
    │       │   │   └── migration.sql
    │       │   ├── 20240917183014_remove_covered_indexes_14
    │       │   │   └── migration.sql
    │       │   ├── 20240917183015_remove_covered_indexes_15
    │       │   │   └── migration.sql
    │       │   ├── 20240917183016_remove_covered_indexes_16
    │       │   │   └── migration.sql
    │       │   ├── 20241009042557_auth_add_created_at_for_gitlab
    │       │   │   └── migration.sql
    │       │   ├── 20241009110720_scores_add_nullable_queue_id_column
    │       │   │   └── migration.sql
    │       │   ├── 20241009113245_add_annotation_queue
    │       │   │   └── migration.sql
    │       │   ├── 20241010120245_llm_keys_add_config
    │       │   │   └── migration.sql
    │       │   ├── 20241015110145_prompts_config_to_JSON
    │       │   │   └── migration.sql
    │       │   ├── 20241022110145_add_claude_sonnet_35
    │       │   │   └── migration.sql
    │       │   ├── 20241023110145_update_claude_sonnet_35
    │       │   │   └── migration.sql
    │       │   ├── 20241024100928_add_prices_table
    │       │   │   └── migration.sql
    │       │   ├── 20241024111800_add_background_migrations_table
    │       │   │   └── migration.sql
    │       │   ├── 20241024121500_add_generations_cost_backfill_background_migration
    │       │   │   └── migration.sql
    │       │   ├── 20241024173000_add_traces_pg_to_ch_background_migration
    │       │   │   └── migration.sql
    │       │   ├── 20241024173700_add_observations_pg_to_ch_background_migration
    │       │   │   └── migration.sql
    │       │   ├── 20241024173800_add_scores_pg_to_ch_background_migration
    │       │   │   └── migration.sql
    │       │   ├── 20241029130802_prices_drop_excess_index
    │       │   │   └── migration.sql
    │       │   ├── 20241104111600_background_migrations_add_state_column
    │       │   │   └── migration.sql
    │       │   ├── 20241105110900_add_claude_haiku_35
    │       │   │   └── migration.sql
    │       │   ├── 20241106122605_add_media_tables
    │       │   │   └── migration.sql
    │       │   ├── 20241114175010_job_executions_add_observation_dataset_item_cols
    │       │   │   └── migration.sql
    │       │   ├── 20241124115100_add_projects_deleted_at
    │       │   │   └── migration.sql
    │       │   ├── 20241125124029_add_chatgpt_4o_prices
    │       │   │   └── migration.sql
    │       │   ├── 20241206115829_remove_trace_score_observation_constraints
    │       │   │   └── migration.sql
    │       │   ├── 20250108220721_add_queue_backup_table
    │       │   │   └── migration.sql
    │       │   ├── 20250109083346_drop_trace_tracesession_fk
    │       │   │   └── migration.sql
    │       │   ├── 20250116154613_add_billing_meter_backups
    │       │   │   └── migration.sql
    │       │   ├── 20250122152102_add_llm_api_keys_extra_headers
    │       │   │   └── migration.sql
    │       │   ├── 20250123103200_add_retention_days_to_projects
    │       │   │   └── migration.sql
    │       │   ├── 20250128144418_llm_adapter_rename_google_vertex_ai
    │       │   │   └── migration.sql
    │       │   ├── 20250128163035_add_nullable_commit_message_prompts
    │       │   │   └── migration.sql
    │       │   ├── 20250204180200_add_event_log_table
    │       │   │   └── migration.sql
    │       │   ├── 20250211102600_drop_event_log_table
    │       │   │   └── migration.sql
    │       │   ├── 20250211123300_drop_events_table
    │       │   │   └── migration.sql
    │       │   ├── 20250214173309_add_timescope_to_configs
    │       │   │   └── migration.sql
    │       │   ├── 20250220141500_add_environment_to_trace_sessions
    │       │   │   └── migration.sql
    │       │   ├── 20250221143400_drop_trace_view_observation_view
    │       │   │   └── migration.sql
    │       │   ├── 20250303144044_add_prompt_dependencies_table
    │       │   │   └── migration.sql
    │       │   ├── 20250310100328_add_api_key_to_audit_log
    │       │   │   └── migration.sql
    │       │   ├── 20250321102240_drop_queue_backup_table
    │       │   │   └── migration.sql
    │       │   ├── 20250324110557_add_blobstorage_integration_table
    │       │   │   └── migration.sql
    │       │   ├── 20250326180640_add_llm_tools_and_schemas_tables
    │       │   │   └── migration.sql
    │       │   ├── 20250401122159_add_prompt_protected_labels_table
    │       │   │   └── migration.sql
    │       │   ├── 20250402142320_add_blobstorage_integration_file_type
    │       │   │   └── migration.sql
    │       │   ├── 20250403153555_membership_invitations_no_duplicates
    │       │   │   └── migration.sql
    │       │   ├── 20250409154352_add_dashboard_data_model
    │       │   │   └── migration.sql
    │       │   ├── 20250410145712_add_organization_scoped_api_keys
    │       │   │   └── migration.sql
    │       │   ├── 20250420120553_add_organization_and_project_metadata
    │       │   │   └── migration.sql
    │       │   ├── 20250517173700_add_event_log_migration_background_migration.sql
    │       │   │   └── migration.sql
    │       │   ├── 20250517273700_add_table_view_presets.sql
    │       │   │   └── migration.sql
    │       │   ├── 20250519073249_add_trace_media_media_id_index
    │       │   │   └── migration.sql
    │       │   ├── 20250519073327_add_observation_media_media_id_index
    │       │   │   └── migration.sql
    │       │   ├── 20250519093327_media_add_index_project_id_id
    │       │   │   └── migration.sql
    │       │   ├── 20250519093328_media_relax_id_uniqueness_to_project_only
    │       │   │   └── migration.sql
    │       │   ├── 20250519145128_resize_dashboard_y_axis_components
    │       │   │   └── migration.sql
    │       │   ├── 20250520123737_add_single_aggregate_chart_type
    │       │   │   └── migration.sql
    │       │   ├── 20250522140357_remove_obsolete_observation_media_index
    │       │   │   └── migration.sql
    │       │   ├── 20250523100511_add_default_eval_model_table
    │       │   │   └── migration.sql
    │       │   ├── 20250523110540_modify_nullable_cols_eval_templates
    │       │   │   └── migration.sql
    │       │   ├── 20250523120545_add_nullable_job_template_id
    │       │   │   └── migration.sql
    │       │   ├── 20250529071241_make_blobstorage_integration_credentials_optional
    │       │   │   └── migration.sql
    │       │   ├── 20250604085536_add_histogram_chart_type
    │       │   │   └── migration.sql
    │       │   └── migration_lock.toml
    │       ├── schema.prisma
    │       └── seed.ts
    │   ├── scripts
    │       ├── cleanup.sql
    │       ├── load-seed.ts
    │       └── prepareClickhouse.ts
    │   ├── src
    │       ├── constants.ts
    │       ├── db.ts
    │       ├── domain
    │       │   ├── index.ts
    │       │   ├── observations.ts
    │       │   ├── scores.ts
    │       │   ├── table-view-presets.ts
    │       │   └── traces.ts
    │       ├── encryption
    │       │   └── index.ts
    │       ├── env.ts
    │       ├── errors
    │       │   ├── ApiError.ts
    │       │   ├── BaseError.ts
    │       │   ├── ConflictError.ts
    │       │   ├── ForbiddenError.ts
    │       │   ├── InternalServerError.ts
    │       │   ├── InvalidRequestError.ts
    │       │   ├── MethodNotAllowedError.ts
    │       │   ├── NotFoundError.ts
    │       │   ├── UnauthorizedError.ts
    │       │   └── index.ts
    │       ├── features
    │       │   ├── annotation
    │       │   │   └── types.ts
    │       │   ├── batchAction
    │       │   │   └── types.ts
    │       │   ├── batchExport
    │       │   │   └── types.ts
    │       │   ├── comments
    │       │   │   └── types.ts
    │       │   ├── entitlements
    │       │   │   └── plans.ts
    │       │   ├── evals
    │       │   │   ├── types.ts
    │       │   │   └── utilities.ts
    │       │   ├── experiments
    │       │   │   └── utils.ts
    │       │   ├── prompts
    │       │   │   └── parsePromptDependencyTags.ts
    │       │   └── scores
    │       │   │   ├── index.ts
    │       │   │   ├── interfaces
    │       │   │       ├── README.md
    │       │   │       ├── api
    │       │   │       │   ├── index.ts
    │       │   │       │   ├── shared.ts
    │       │   │       │   ├── v1
    │       │   │       │   │   ├── endpoints.ts
    │       │   │       │   │   ├── schemas.ts
    │       │   │       │   │   └── validation.ts
    │       │   │       │   └── v2
    │       │   │       │   │   ├── endpoints.ts
    │       │   │       │   │   ├── schemas.ts
    │       │   │       │   │   └── validation.ts
    │       │   │       ├── application
    │       │   │       │   └── validation.ts
    │       │   │       ├── index.ts
    │       │   │       ├── ingestion
    │       │   │       │   └── validation.ts
    │       │   │       ├── shared.ts
    │       │   │       └── ui
    │       │   │       │   └── types.ts
    │       │   │   └── scoreConfigTypes.ts
    │       ├── index.ts
    │       ├── interfaces
    │       │   ├── cloudConfigSchema.ts
    │       │   ├── customLLMProviderConfigSchemas.ts
    │       │   ├── filters.ts
    │       │   ├── orderBy.ts
    │       │   ├── parseDbOrg.ts
    │       │   ├── rate-limits.ts
    │       │   ├── search.ts
    │       │   └── tableNames.ts
    │       ├── observationsTable.ts
    │       ├── server
    │       │   ├── auth
    │       │   │   ├── apiKeys.ts
    │       │   │   ├── customSsoProvider.ts
    │       │   │   ├── gitHubEnterpriseProvider.ts
    │       │   │   └── types.ts
    │       │   ├── clickhouse
    │       │   │   ├── client.ts
    │       │   │   ├── schema.ts
    │       │   │   └── schemaUtils.ts
    │       │   ├── data-deletion
    │       │   │   └── ingestionFileDeletion.ts
    │       │   ├── filterToPrisma.ts
    │       │   ├── headerPropagation.ts
    │       │   ├── index.ts
    │       │   ├── ingestion
    │       │   │   ├── processEventBatch.ts
    │       │   │   ├── types.ts
    │       │   │   └── validateAndInflateScore.ts
    │       │   ├── instrumentation
    │       │   │   ├── README.md
    │       │   │   └── index.ts
    │       │   ├── llm
    │       │   │   ├── fetchLLMCompletion.ts
    │       │   │   ├── types.ts
    │       │   │   └── utils.ts
    │       │   ├── logger.ts
    │       │   ├── orderByToPrisma.ts
    │       │   ├── queries
    │       │   │   ├── clickhouse-sql
    │       │   │   │   ├── clickhouse-filter.ts
    │       │   │   │   ├── factory.ts
    │       │   │   │   ├── orderby-factory.ts
    │       │   │   │   └── search.ts
    │       │   │   ├── createGenerationsQuery.ts
    │       │   │   ├── createSessionsAllQuery.ts
    │       │   │   ├── index.ts
    │       │   │   └── types.ts
    │       │   ├── queues.ts
    │       │   ├── redis
    │       │   │   ├── batchActionQueue.ts
    │       │   │   ├── batchExport.ts
    │       │   │   ├── blobStorageIntegrationProcessingQueue.ts
    │       │   │   ├── blobStorageIntegrationQueue.ts
    │       │   │   ├── cloudUsageMeteringQueue.ts
    │       │   │   ├── coreDataS3ExportQueue.ts
    │       │   │   ├── createEvalQueue.ts
    │       │   │   ├── dataRetentionProcessingQueue.ts
    │       │   │   ├── dataRetentionQueue.ts
    │       │   │   ├── datasetRunItemUpsert.ts
    │       │   │   ├── dlqRetryQueue.ts
    │       │   │   ├── evalExecutionQueue.ts
    │       │   │   ├── experimentCreateQueue.ts
    │       │   │   ├── getQueue.ts
    │       │   │   ├── ingestionQueue.ts
    │       │   │   ├── meteringDataPostgresExportQueue.ts
    │       │   │   ├── postHogIntegrationProcessingQueue.ts
    │       │   │   ├── postHogIntegrationQueue.ts
    │       │   │   ├── projectDelete.ts
    │       │   │   ├── redis.ts
    │       │   │   ├── scoreDelete.ts
    │       │   │   ├── traceDelete.ts
    │       │   │   └── traceUpsert.ts
    │       │   ├── repositories
    │       │   │   ├── README.md
    │       │   │   ├── blobStorageLog.ts
    │       │   │   ├── clickhouse.ts
    │       │   │   ├── constants.ts
    │       │   │   ├── dashboards.ts
    │       │   │   ├── definitions.ts
    │       │   │   ├── environments.ts
    │       │   │   ├── index.ts
    │       │   │   ├── observations.ts
    │       │   │   ├── observations_converters.ts
    │       │   │   ├── scores-utils.ts
    │       │   │   ├── scores.ts
    │       │   │   ├── scores_converters.ts
    │       │   │   ├── trace-sessions.ts
    │       │   │   ├── traces.ts
    │       │   │   ├── traces_converters.ts
    │       │   │   └── types.ts
    │       │   ├── s3
    │       │   │   └── index.ts
    │       │   ├── services
    │       │   │   ├── DashboardService
    │       │   │   │   ├── DashboardService.ts
    │       │   │   │   ├── index.ts
    │       │   │   │   └── types.ts
    │       │   │   ├── DefaultEvaluationModelService
    │       │   │   │   ├── DefaultEvalModelService.ts
    │       │   │   │   └── index.ts
    │       │   │   ├── PromptService
    │       │   │   │   ├── index.ts
    │       │   │   │   ├── types.ts
    │       │   │   │   └── utils.ts
    │       │   │   ├── StorageService.ts
    │       │   │   ├── TableViewService
    │       │   │   │   ├── TableViewService.ts
    │       │   │   │   ├── index.ts
    │       │   │   │   └── types.ts
    │       │   │   ├── datasets-ui-table-service.ts
    │       │   │   ├── email
    │       │   │   │   ├── batchExportSuccess
    │       │   │   │   │   ├── BatchExportSuccessEmailTemplate.tsx
    │       │   │   │   │   └── sendBatchExportSuccessEmail.ts
    │       │   │   │   ├── organizationInvitation
    │       │   │   │   │   ├── MembershipInvitationEmailTemplate.tsx
    │       │   │   │   │   └── sendMembershipInvitationEmail.ts
    │       │   │   │   └── passwordReset
    │       │   │   │   │   └── sendResetPasswordVerificationRequest.tsx
    │       │   │   ├── sessions-ui-table-service.ts
    │       │   │   └── traces-ui-table-service.ts
    │       │   ├── test-utils
    │       │   │   ├── clickhouse-helpers.ts
    │       │   │   ├── index.ts
    │       │   │   ├── org-factory.ts
    │       │   │   └── tracing-factory.ts
    │       │   └── utils
    │       │   │   ├── DatabaseReadStream.ts
    │       │   │   ├── metadata_conversion.ts
    │       │   │   └── transforms
    │       │   │       ├── index.ts
    │       │   │       ├── stringify.ts
    │       │   │       ├── transformStreamToCsv.ts
    │       │   │       ├── transformStreamToJson.ts
    │       │   │       └── transformStreamToJsonl.ts
    │       ├── tableDefinitions
    │       │   ├── index.ts
    │       │   ├── mapDashboards.ts
    │       │   ├── mapObservationsTable.ts
    │       │   ├── mapScoresTable.ts
    │       │   ├── mapSessionTable.ts
    │       │   ├── mapTracesTable.ts
    │       │   ├── sessionsView.ts
    │       │   ├── tracesTable.ts
    │       │   ├── typeHelpers.ts
    │       │   └── types.ts
    │       ├── types.ts
    │       └── utils
    │       │   ├── environment.ts
    │       │   ├── json.ts
    │       │   ├── objects.ts
    │       │   ├── scores.ts
    │       │   ├── stringChecks.ts
    │       │   ├── typeChecks.ts
    │       │   └── zod.ts
    │   └── tsconfig.json
├── patches
    └── next-auth@4.24.11.patch
├── pnpm-lock.yaml
├── pnpm-workspace.yaml
├── scripts
    └── nuke.sh
├── turbo.json
├── web
    ├── .eslintrc.js
    ├── Dockerfile
    ├── components.json
    ├── entrypoint.sh
    ├── jest.config.mjs
    ├── next.config.mjs
    ├── package.json
    ├── playwright.config.ts
    ├── postcss.config.cjs
    ├── prettier.config.cjs
    ├── public
    │   ├── android-chrome-192x192.png
    │   ├── apple-touch-icon.png
    │   ├── assets
    │   │   ├── huggingface-logo.svg
    │   │   └── ragas-logo.png
    │   ├── favicon-16x16.png
    │   ├── favicon-32x32.png
    │   ├── favicon.ico
    │   ├── generated
    │   │   ├── api-client
    │   │   │   └── openapi.yml
    │   │   ├── api
    │   │   │   └── openapi.yml
    │   │   ├── organizations-api
    │   │   │   └── openapi.yml
    │   │   ├── organizations-postman
    │   │   │   └── collection.json
    │   │   └── postman
    │   │   │   └── collection.json
    │   ├── icon.svg
    │   └── icon256.png
    ├── sentry.client.config.ts
    ├── src
    │   ├── __e2e__
    │   │   ├── api.servertest.ts
    │   │   ├── auth.spec.ts
    │   │   └── create-project.spec.ts
    │   ├── __tests__
    │   │   ├── after-teardown.ts
    │   │   ├── aggregateScores.clienttest.ts
    │   │   ├── annotation-queues-api.servertest.ts
    │   │   ├── api-auth.servertest.ts
    │   │   ├── async
    │   │   │   ├── comments-api.servertest.ts
    │   │   │   ├── daily-metrics-api.servertest.ts
    │   │   │   ├── dataset-service.servertest.ts
    │   │   │   ├── datasets-api.servertest.ts
    │   │   │   ├── datasets-ui-table.servertest.ts
    │   │   │   ├── evals-trpc.servertest.ts
    │   │   │   ├── ingestion-api.servertest.ts
    │   │   │   ├── memberships-api.servertest.ts
    │   │   │   ├── metrics-api.servertest.ts
    │   │   │   ├── observation-api.servertest.ts
    │   │   │   ├── organizations-api-key-trpc.servertest.ts
    │   │   │   ├── organizations-api.servertest.ts
    │   │   │   ├── projects-api.servertest.ts
    │   │   │   ├── repositories
    │   │   │   │   ├── dashboard-repository.servertest.ts
    │   │   │   │   ├── environment-repository.servertest.ts
    │   │   │   │   ├── observation-repository.servertest.ts
    │   │   │   │   ├── score-repository.servertest.ts
    │   │   │   │   └── trace-repository.servertest.ts
    │   │   │   ├── scim-api.servertest.ts
    │   │   │   ├── scores-api-v1.servertest.ts
    │   │   │   ├── scores-api-v2.servertest.ts
    │   │   │   ├── scores-trpc.servertest.ts
    │   │   │   ├── sessions-api.servertest.ts
    │   │   │   ├── sessions-trpc.servertest.ts
    │   │   │   ├── sessions-ui-table.servertest.ts
    │   │   │   ├── traces-api.servertest.ts
    │   │   │   ├── traces-trpc.servertest.ts
    │   │   │   ├── traces-ui-table.servertest.ts
    │   │   │   └── users-ui-table.servertest.ts
    │   │   ├── dom.clienttest.ts
    │   │   ├── fixtures
    │   │   │   └── TestRouter.ts
    │   │   ├── ingestion-unit.servertest.ts
    │   │   ├── llm-api-key.servertest.ts
    │   │   ├── markdown.clienttest.ts
    │   │   ├── media.servertest.ts
    │   │   ├── model-definitions.servertest.ts
    │   │   ├── orderByToPrisma.servertest.ts
    │   │   ├── promptCache.servertest.ts
    │   │   ├── prompts.v1.servertest.ts
    │   │   ├── prompts.v2.servertest.ts
    │   │   ├── queryBuilder.servertest.ts
    │   │   ├── queryBuilderDashboards.servertest.ts
    │   │   ├── queryBuilderSQLI.servertest.ts
    │   │   ├── rate-limit.servertest.ts
    │   │   ├── score-configs.servertest.ts
    │   │   ├── server
    │   │   │   └── api
    │   │   │   │   ├── otel
    │   │   │   │       └── otelMapping.servertest.ts
    │   │   │   │   └── tables
    │   │   │   │       └── prompts-ui.servertest.ts
    │   │   ├── sessions.servertest.ts
    │   │   ├── static
    │   │   │   ├── bitcoin.pdf
    │   │   │   └── langfuse-logo.png
    │   │   ├── table-view-presets.clienttest.ts
    │   │   ├── teardown.ts
    │   │   ├── test-utils.ts
    │   │   └── zod.servertest.ts
    │   ├── app
    │   │   ├── api
    │   │   │   ├── billing
    │   │   │   │   └── stripe-webhook
    │   │   │   │   │   └── route.ts
    │   │   │   └── chatCompletion
    │   │   │   │   └── route.ts
    │   │   └── layout.tsx
    │   ├── components
    │   │   ├── ActionButton.tsx
    │   │   ├── BatchExportTableButton.tsx
    │   │   ├── ChatMessages
    │   │   │   ├── ChatMessageComponent.tsx
    │   │   │   ├── ToolCallCard.tsx
    │   │   │   ├── index.tsx
    │   │   │   ├── types.ts
    │   │   │   └── utils
    │   │   │   │   └── createEmptyMessage.ts
    │   │   ├── DiffViewer.tsx
    │   │   ├── EnvLabel.tsx
    │   │   ├── ItemBadge.tsx
    │   │   ├── LangfuseLogo.tsx
    │   │   ├── LocalIsoDate.tsx
    │   │   ├── ModelParameters
    │   │   │   ├── LLMApiKeyComponent.tsx
    │   │   │   └── index.tsx
    │   │   ├── NoDataOrLoading.tsx
    │   │   ├── PagedSettingsContainer.tsx
    │   │   ├── PosthogLogo.tsx
    │   │   ├── SettingsDangerZone.tsx
    │   │   ├── Slider.tsx
    │   │   ├── VersionLabel.tsx
    │   │   ├── date-picker.tsx
    │   │   ├── date-range-dropdowns.tsx
    │   │   ├── deleteButton.tsx
    │   │   ├── editor
    │   │   │   ├── CodeMirrorEditor.tsx
    │   │   │   ├── PromptLinkingEditor.tsx
    │   │   │   ├── dark-theme.ts
    │   │   │   ├── index.ts
    │   │   │   ├── light-theme.ts
    │   │   │   └── shared-theme.ts
    │   │   ├── error-page.tsx
    │   │   ├── grouped-score-badge.tsx
    │   │   ├── images
    │   │   │   ├── product_hunt_badge_dark.svg
    │   │   │   └── product_hunt_badge_light.svg
    │   │   ├── layouts
    │   │   │   ├── README.md
    │   │   │   ├── breadcrumb.tsx
    │   │   │   ├── container-page.tsx
    │   │   │   ├── doc-popup.tsx
    │   │   │   ├── header.tsx
    │   │   │   ├── layout.tsx
    │   │   │   ├── page-header.tsx
    │   │   │   ├── page.tsx
    │   │   │   ├── routes.tsx
    │   │   │   ├── settings-table-card.tsx
    │   │   │   ├── spinner.tsx
    │   │   │   └── status-badge.tsx
    │   │   ├── level-colors.tsx
    │   │   ├── level-counts-display.tsx
    │   │   ├── nav
    │   │   │   ├── app-sidebar.tsx
    │   │   │   ├── nav-main.tsx
    │   │   │   ├── nav-user.tsx
    │   │   │   ├── sidebar-notifications.tsx
    │   │   │   └── support-menu-dropdown.tsx
    │   │   ├── onboarding
    │   │   │   ├── AnnotationQueuesOnboarding.tsx
    │   │   │   ├── DatasetsOnboarding.tsx
    │   │   │   ├── EvaluatorsOnboarding.tsx
    │   │   │   ├── PromptsOnboarding.tsx
    │   │   │   ├── ScoresOnboarding.tsx
    │   │   │   ├── SessionsOnboarding.tsx
    │   │   │   ├── TracesOnboarding.tsx
    │   │   │   └── UsersOnboarding.tsx
    │   │   ├── projectNavigation.tsx
    │   │   ├── publish-object-switch.tsx
    │   │   ├── schemas
    │   │   │   ├── ChatMlSchema.ts
    │   │   │   └── MarkdownSchema.ts
    │   │   ├── scores-table-cell.tsx
    │   │   ├── session
    │   │   │   └── index.tsx
    │   │   ├── star-toggle.tsx
    │   │   ├── stats-cards.tsx
    │   │   ├── table
    │   │   │   ├── data-table-column-visibility-filter.tsx
    │   │   │   ├── data-table-multi-select-actions
    │   │   │   │   └── data-table-select-all-banner.tsx
    │   │   │   ├── data-table-pagination.tsx
    │   │   │   ├── data-table-row-height-switch.tsx
    │   │   │   ├── data-table-toolbar.tsx
    │   │   │   ├── data-table.tsx
    │   │   │   ├── peek.tsx
    │   │   │   ├── peek
    │   │   │   │   ├── hooks
    │   │   │   │   │   ├── useDatasetComparePeekNavigation.ts
    │   │   │   │   │   ├── useDatasetComparePeekState.ts
    │   │   │   │   │   ├── useEvalTemplatesPeekNavigation.ts
    │   │   │   │   │   ├── useObservationPeekNavigation.ts
    │   │   │   │   │   ├── useObservationPeekState.ts
    │   │   │   │   │   ├── usePeekData.ts
    │   │   │   │   │   ├── usePeekEvalConfigData.ts
    │   │   │   │   │   ├── usePeekEvalTemplateData.ts
    │   │   │   │   │   ├── usePeekState.ts
    │   │   │   │   │   ├── usePeekView.ts
    │   │   │   │   │   ├── useRunningEvaluatorsPeekNavigation.ts
    │   │   │   │   │   ├── useTracePeekNavigation.ts
    │   │   │   │   │   └── useTracePeekState.ts
    │   │   │   │   ├── peek-dataset-compare-detail.tsx
    │   │   │   │   ├── peek-evaluator-config-detail.tsx
    │   │   │   │   ├── peek-evaluator-template-detail.tsx
    │   │   │   │   ├── peek-observation-detail.tsx
    │   │   │   │   └── peek-trace-detail.tsx
    │   │   │   ├── table-id.tsx
    │   │   │   ├── table-link.tsx
    │   │   │   ├── table-view-presets
    │   │   │   │   ├── README.md
    │   │   │   │   ├── components
    │   │   │   │   │   └── data-table-view-presets-drawer.tsx
    │   │   │   │   ├── hooks
    │   │   │   │   │   ├── useTableViewManager.ts
    │   │   │   │   │   ├── useViewData.ts
    │   │   │   │   │   └── useViewMutations.ts
    │   │   │   │   └── validation.ts
    │   │   │   ├── types.ts
    │   │   │   ├── use-cases
    │   │   │   │   ├── models.tsx
    │   │   │   │   ├── observations.tsx
    │   │   │   │   ├── score-configs.tsx
    │   │   │   │   ├── scores.tsx
    │   │   │   │   ├── sessions.tsx
    │   │   │   │   ├── traces.tsx
    │   │   │   │   └── useFullTextSearch.tsx
    │   │   │   └── utils
    │   │   │   │   └── joinTableCoreAndMetrics.ts
    │   │   ├── token-usage-badge.tsx
    │   │   ├── trace
    │   │   │   ├── BreakdownToolTip.tsx
    │   │   │   ├── CopyIdsPopover.tsx
    │   │   │   ├── IOPreview.tsx
    │   │   │   ├── ObservationPreview.tsx
    │   │   │   ├── ObservationTree.tsx
    │   │   │   ├── TracePage.tsx
    │   │   │   ├── TracePreview.tsx
    │   │   │   ├── TraceTimelineView.tsx
    │   │   │   ├── index.tsx
    │   │   │   └── lib
    │   │   │   │   └── helpers.ts
    │   │   ├── ui
    │   │   │   ├── CodeJsonViewer.tsx
    │   │   │   ├── Codeblock.tsx
    │   │   │   ├── LangfuseMediaView.tsx
    │   │   │   ├── MarkdownJsonView.tsx
    │   │   │   ├── MarkdownViewer.tsx
    │   │   │   ├── accordion.tsx
    │   │   │   ├── alert.tsx
    │   │   │   ├── avatar.tsx
    │   │   │   ├── badge.tsx
    │   │   │   ├── breadcrumb.tsx
    │   │   │   ├── button.tsx
    │   │   │   ├── calendar.tsx
    │   │   │   ├── card.tsx
    │   │   │   ├── chart.tsx
    │   │   │   ├── checkbox.tsx
    │   │   │   ├── collapsible.tsx
    │   │   │   ├── command.tsx
    │   │   │   ├── dialog.tsx
    │   │   │   ├── drawer.tsx
    │   │   │   ├── dropdown-menu.tsx
    │   │   │   ├── form.tsx
    │   │   │   ├── hover-card.tsx
    │   │   │   ├── input-command.tsx
    │   │   │   ├── input.tsx
    │   │   │   ├── label.tsx
    │   │   │   ├── password-input.tsx
    │   │   │   ├── popover.tsx
    │   │   │   ├── progress.tsx
    │   │   │   ├── radio-group.tsx
    │   │   │   ├── resizable-image.tsx
    │   │   │   ├── resizable.tsx
    │   │   │   ├── scroll-area.tsx
    │   │   │   ├── select.tsx
    │   │   │   ├── separator.tsx
    │   │   │   ├── sheet.tsx
    │   │   │   ├── side-panel.tsx
    │   │   │   ├── sidebar.tsx
    │   │   │   ├── skeleton.tsx
    │   │   │   ├── slider.tsx
    │   │   │   ├── sonner.tsx
    │   │   │   ├── splash-screen.tsx
    │   │   │   ├── switch.tsx
    │   │   │   ├── table.tsx
    │   │   │   ├── tabs-bar.tsx
    │   │   │   ├── tabs.tsx
    │   │   │   ├── textarea.tsx
    │   │   │   ├── time-icon.tsx
    │   │   │   ├── time-period-select.tsx
    │   │   │   ├── time-picker-input.tsx
    │   │   │   ├── time-picker-utils.tsx
    │   │   │   ├── time-picker.tsx
    │   │   │   ├── timeline.tsx
    │   │   │   ├── toggle-group.tsx
    │   │   │   ├── toggle.tsx
    │   │   │   └── tooltip.tsx
    │   │   ├── useLocalStorage.tsx
    │   │   └── useSessionStorage.tsx
    │   ├── constants
    │   │   ├── VERSION.ts
    │   │   └── index.ts
    │   ├── ee
    │   │   ├── README.md
    │   │   └── features
    │   │   │   ├── audit-log-viewer
    │   │   │       ├── AuditLogsSettingsPage.tsx
    │   │   │       └── AuditLogsTable.tsx
    │   │   │   ├── billing
    │   │   │       ├── README.md
    │   │   │       ├── components
    │   │   │       │   ├── BillingSettings.tsx
    │   │   │       │   ├── SupportOrUpgradePage.tsx
    │   │   │       │   └── UsageTracker.tsx
    │   │   │       ├── constants.ts
    │   │   │       ├── server
    │   │   │       │   ├── cloudBillingRouter.ts
    │   │   │       │   └── stripeWebhookApiHandler.ts
    │   │   │       ├── stripeClientReference.ts
    │   │   │       └── utils
    │   │   │       │   ├── stripe.ts
    │   │   │       │   └── stripeProducts.ts
    │   │   │   ├── multi-tenant-sso
    │   │   │       ├── createNewSsoConfigHandler.ts
    │   │   │       ├── multiTenantSsoAvailable.ts
    │   │   │       ├── types.ts
    │   │   │       └── utils.ts
    │   │   │   ├── sso-settings
    │   │   │       └── components
    │   │   │       │   └── SSOSettings.tsx
    │   │   │   └── ui-customization
    │   │   │       ├── productModuleSchema.ts
    │   │   │       ├── uiCustomizationRouter.ts
    │   │   │       └── useUiCustomization.ts
    │   ├── env.mjs
    │   ├── features
    │   │   ├── README.md
    │   │   ├── admin-api
    │   │   │   ├── memberships.ts
    │   │   │   ├── organizations
    │   │   │   │   ├── apiKeys
    │   │   │   │   │   ├── apiKeyById.ts
    │   │   │   │   │   └── index.ts
    │   │   │   │   ├── index.ts
    │   │   │   │   └── organizationById.ts
    │   │   │   ├── projects.ts
    │   │   │   ├── projects
    │   │   │   │   ├── createProject.ts
    │   │   │   │   └── projectById
    │   │   │   │   │   ├── apiKeys
    │   │   │   │   │       ├── apiKeyById.ts
    │   │   │   │   │       └── index.ts
    │   │   │   │   │   ├── index.ts
    │   │   │   │   │   └── memberships
    │   │   │   │   │       └── index.ts
    │   │   │   └── server
    │   │   │   │   └── adminApiAuth.ts
    │   │   ├── annotation-queues
    │   │   │   ├── components
    │   │   │   │   ├── AnnotationQueueItemPage.tsx
    │   │   │   │   ├── AnnotationQueueItemsTable.tsx
    │   │   │   │   ├── AnnotationQueuesItem.tsx
    │   │   │   │   ├── AnnotationQueuesTable.tsx
    │   │   │   │   ├── CreateNewAnnotationQueueItem.tsx
    │   │   │   │   ├── CreateOrEditAnnotationQueueButton.tsx
    │   │   │   │   └── DeleteAnnotationQueueButton.tsx
    │   │   │   ├── pages
    │   │   │   │   ├── AnnotationQueueItems.tsx
    │   │   │   │   └── AnnotationQueues.tsx
    │   │   │   └── server
    │   │   │   │   ├── annotationQueueItems.ts
    │   │   │   │   └── annotationQueues.ts
    │   │   ├── audit-logs
    │   │   │   └── auditLog.ts
    │   │   ├── auth-credentials
    │   │   │   ├── components
    │   │   │   │   ├── ResetPasswordButton.tsx
    │   │   │   │   └── ResetPasswordPage.tsx
    │   │   │   ├── lib
    │   │   │   │   ├── credentialsServerUtils.ts
    │   │   │   │   └── credentialsUtils.ts
    │   │   │   └── server
    │   │   │   │   ├── credentialsRouter.ts
    │   │   │   │   └── signupApiHandler.ts
    │   │   ├── auth
    │   │   │   ├── components
    │   │   │   │   ├── AuthCloudPrivacyNotice.tsx
    │   │   │   │   └── AuthCloudRegionSwitch.tsx
    │   │   │   ├── hooks.ts
    │   │   │   └── lib
    │   │   │   │   ├── createProjectMembershipsOnSignup.ts
    │   │   │   │   ├── projectNameSchema.ts
    │   │   │   │   ├── projectRetentionSchema.ts
    │   │   │   │   └── signupSchema.ts
    │   │   ├── background-migrations
    │   │   │   ├── components
    │   │   │   │   ├── background-migrations.tsx
    │   │   │   │   └── retry-background-migration.tsx
    │   │   │   └── server
    │   │   │   │   └── background-migrations-router.ts
    │   │   ├── batch-exports
    │   │   │   ├── README.md
    │   │   │   ├── components
    │   │   │   │   ├── BatchExportsSettingsPage.tsx
    │   │   │   │   └── BatchExportsTable.tsx
    │   │   │   └── server
    │   │   │   │   └── batchExport.ts
    │   │   ├── blobstorage-integration
    │   │   │   ├── blobstorage-integration-router.ts
    │   │   │   └── types.ts
    │   │   ├── cloud-status-notification
    │   │   │   ├── components
    │   │   │   │   └── CloudStatusMenu.tsx
    │   │   │   ├── server
    │   │   │   │   └── cloud-status-router.ts
    │   │   │   └── types.ts
    │   │   ├── column-visibility
    │   │   │   └── hooks
    │   │   │   │   ├── useColumnOrder.ts
    │   │   │   │   └── useColumnVisibility.ts
    │   │   ├── command-k-menu
    │   │   │   ├── CommandMenu.tsx
    │   │   │   └── CommandMenuProvider.tsx
    │   │   ├── comments
    │   │   │   ├── CommentCountIcon.tsx
    │   │   │   ├── CommentDrawerButton.tsx
    │   │   │   ├── CommentList.tsx
    │   │   │   └── validateCommentReferenceObject.ts
    │   │   ├── dashboard
    │   │   │   ├── components
    │   │   │   │   ├── BaseTimeSeriesChart.tsx
    │   │   │   │   ├── ChartScores.tsx
    │   │   │   │   ├── DashboardTable.tsx
    │   │   │   │   ├── EditDashboardDialog.tsx
    │   │   │   │   ├── LatencyChart.tsx
    │   │   │   │   ├── LatencyTables.tsx
    │   │   │   │   ├── LeftAlignedCell.tsx
    │   │   │   │   ├── ModelCostTable.tsx
    │   │   │   │   ├── ModelSelector.tsx
    │   │   │   │   ├── ModelUsageChart.tsx
    │   │   │   │   ├── RightAlignedCell.tsx
    │   │   │   │   ├── ScoresTable.tsx
    │   │   │   │   ├── SelectDashboardDialog.tsx
    │   │   │   │   ├── TabTimeSeriesChart.tsx
    │   │   │   │   ├── TabsComponent.tsx
    │   │   │   │   ├── Tooltip.tsx
    │   │   │   │   ├── TotalMetric.tsx
    │   │   │   │   ├── TracesBarListChart.tsx
    │   │   │   │   ├── TracesTimeSeriesChart.tsx
    │   │   │   │   ├── UserChart.tsx
    │   │   │   │   ├── cards
    │   │   │   │   │   ├── ChevronButton.tsx
    │   │   │   │   │   ├── DashboardCard.tsx
    │   │   │   │   │   └── DashboardTable.tsx
    │   │   │   │   ├── hooks.ts
    │   │   │   │   └── score-analytics
    │   │   │   │   │   ├── CategoricalScoreChart.tsx
    │   │   │   │   │   ├── NumericScoreHistogram.tsx
    │   │   │   │   │   ├── NumericScoreTimeSeriesChart.tsx
    │   │   │   │   │   └── ScoreAnalytics.tsx
    │   │   │   ├── lib
    │   │   │   │   ├── dashboard-utils.ts
    │   │   │   │   └── score-analytics-utils.ts
    │   │   │   ├── server
    │   │   │   │   └── dashboard-router.ts
    │   │   │   └── utils
    │   │   │   │   └── getColorsForCategories.tsx
    │   │   ├── datasets
    │   │   │   ├── components
    │   │   │   │   ├── DatasetActionButton.tsx
    │   │   │   │   ├── DatasetAggregateTableCell.tsx
    │   │   │   │   ├── DatasetAnalytics.tsx
    │   │   │   │   ├── DatasetCompareRunsTable.tsx
    │   │   │   │   ├── DatasetForm.tsx
    │   │   │   │   ├── DatasetItemsTable.tsx
    │   │   │   │   ├── DatasetRunAggregateColumnHelpers.tsx
    │   │   │   │   ├── DatasetRunItemsTable.tsx
    │   │   │   │   ├── DatasetRunsTable.tsx
    │   │   │   │   ├── DatasetsTable.tsx
    │   │   │   │   ├── DeleteDatasetRunButton.tsx
    │   │   │   │   ├── DuplicateDatasetButton.tsx
    │   │   │   │   ├── EditDatasetItem.tsx
    │   │   │   │   ├── ImportCard.tsx
    │   │   │   │   ├── NewDatasetItemButton.tsx
    │   │   │   │   ├── NewDatasetItemForm.tsx
    │   │   │   │   ├── NewDatasetItemFromExistingObject.tsx
    │   │   │   │   ├── PreviewCsvImport.tsx
    │   │   │   │   ├── UploadDatasetCsv.tsx
    │   │   │   │   └── UploadDatasetCsvButton.tsx
    │   │   │   ├── hooks
    │   │   │   │   └── useDatasetRunAggregateColumns.ts
    │   │   │   ├── lib
    │   │   │   │   ├── csvHelpers.ts
    │   │   │   │   └── findDefaultColumn.ts
    │   │   │   └── server
    │   │   │   │   ├── dataset-router.ts
    │   │   │   │   └── service.ts
    │   │   ├── entitlements
    │   │   │   ├── README.md
    │   │   │   ├── constants
    │   │   │   │   └── entitlements.ts
    │   │   │   ├── hooks.ts
    │   │   │   └── server
    │   │   │   │   ├── getPlan.ts
    │   │   │   │   ├── hasEntitlement.ts
    │   │   │   │   └── hasEntitlementLimit.ts
    │   │   ├── evals
    │   │   │   ├── components
    │   │   │   │   ├── deactivate-config.tsx
    │   │   │   │   ├── eval-form-descriptions.tsx
    │   │   │   │   ├── eval-log.tsx
    │   │   │   │   ├── eval-template-detail.tsx
    │   │   │   │   ├── eval-templates-table.tsx
    │   │   │   │   ├── evaluation-prompt-preview.tsx
    │   │   │   │   ├── evaluator-detail.tsx
    │   │   │   │   ├── evaluator-form.tsx
    │   │   │   │   ├── evaluator-selector.tsx
    │   │   │   │   ├── evaluator-table.tsx
    │   │   │   │   ├── execution-count-tooltip.tsx
    │   │   │   │   ├── inner-evaluator-form.tsx
    │   │   │   │   ├── maintainer-tooltip.tsx
    │   │   │   │   ├── manage-default-eval-model.tsx
    │   │   │   │   ├── ragas-logo.tsx
    │   │   │   │   ├── run-evaluator-form.tsx
    │   │   │   │   ├── select-evaluator-list.tsx
    │   │   │   │   ├── set-up-default-eval-model-card.tsx
    │   │   │   │   ├── template-form.tsx
    │   │   │   │   └── template-selector.tsx
    │   │   │   ├── hooks
    │   │   │   │   ├── useEvalConfigMappingData.ts
    │   │   │   │   ├── useEvalTargetCount.ts
    │   │   │   │   ├── useEvaluationModel.ts
    │   │   │   │   ├── useExtractVariables.ts
    │   │   │   │   ├── useSingleTemplateValidation.ts
    │   │   │   │   ├── useTemplateValidation.ts
    │   │   │   │   ├── useTemplatesValidation.ts
    │   │   │   │   └── useValidateCustomModel.ts
    │   │   │   ├── pages
    │   │   │   │   ├── default-evaluation-model.tsx
    │   │   │   │   ├── evaluators.tsx
    │   │   │   │   ├── new-evaluator.tsx
    │   │   │   │   ├── new-template.tsx
    │   │   │   │   └── templates.tsx
    │   │   │   ├── server
    │   │   │   │   ├── addDatasetRunItemsToEvalQueue.ts
    │   │   │   │   ├── defaultEvalModelRouter.ts
    │   │   │   │   └── router.ts
    │   │   │   ├── types.ts
    │   │   │   └── utils
    │   │   │   │   ├── evaluator-form-utils.ts
    │   │   │   │   ├── job-execution-utils.ts
    │   │   │   │   └── typeHelpers.ts
    │   │   ├── experiments
    │   │   │   ├── components
    │   │   │   │   └── CreateExperimentsForm.tsx
    │   │   │   ├── hooks
    │   │   │   │   ├── useEvaluatorDefaults.ts
    │   │   │   │   ├── useExperimentEvaluatorData.ts
    │   │   │   │   ├── useExperimentEvaluatorSelection.ts
    │   │   │   │   ├── useExperimentNameValidation.ts
    │   │   │   │   └── useExperimentPromptData.ts
    │   │   │   ├── server
    │   │   │   │   └── router.ts
    │   │   │   └── utils
    │   │   │   │   └── evaluatorMappingUtils.ts
    │   │   ├── feature-flags
    │   │   │   ├── README.md
    │   │   │   ├── available-flags.ts
    │   │   │   ├── components
    │   │   │   │   └── FeatureFlagToggle.tsx
    │   │   │   ├── hooks
    │   │   │   │   └── useIsFeatureEnabled.ts
    │   │   │   ├── types.ts
    │   │   │   └── utils.ts
    │   │   ├── feedback
    │   │   │   ├── component
    │   │   │   │   └── FeedbackButton.tsx
    │   │   │   └── server
    │   │   │   │   ├── corsMiddleware.ts
    │   │   │   │   └── feedbackHandler.ts
    │   │   ├── filters
    │   │   │   ├── components
    │   │   │   │   ├── filter-builder.tsx
    │   │   │   │   └── multi-select.tsx
    │   │   │   └── hooks
    │   │   │   │   └── useFilterState.ts
    │   │   ├── llm-api-key
    │   │   │   ├── server
    │   │   │   │   └── router.ts
    │   │   │   └── types.ts
    │   │   ├── llm-schemas
    │   │   │   ├── server
    │   │   │   │   └── router.ts
    │   │   │   └── validation.ts
    │   │   ├── llm-tools
    │   │   │   ├── server
    │   │   │   │   └── router.ts
    │   │   │   └── validation.ts
    │   │   ├── media
    │   │   │   ├── server
    │   │   │   │   ├── getFileExtensionFromContentType.ts
    │   │   │   │   └── getMediaStorageClient.ts
    │   │   │   └── validation.ts
    │   │   ├── models
    │   │   │   ├── components
    │   │   │   │   ├── CloneModelButton.tsx
    │   │   │   │   ├── DeleteModelButton.tsx
    │   │   │   │   ├── EditModelButton.tsx
    │   │   │   │   ├── ModelSettings.tsx
    │   │   │   │   ├── PriceBreakdownTooltip.tsx
    │   │   │   │   ├── PricePreview.tsx
    │   │   │   │   ├── PriceUnitSelector.tsx
    │   │   │   │   └── UpsertModelFormDrawer.tsx
    │   │   │   ├── hooks
    │   │   │   │   └── usePriceUnitMultiplier.ts
    │   │   │   ├── server
    │   │   │   │   └── isValidPostgresRegex.ts
    │   │   │   ├── utils.ts
    │   │   │   └── validation.ts
    │   │   ├── navigate-detail-pages
    │   │   │   ├── DetailPageNav.tsx
    │   │   │   └── context.tsx
    │   │   ├── notifications
    │   │   │   ├── ErrorNotification.tsx
    │   │   │   ├── Notification.tsx
    │   │   │   ├── SuccessNotification.tsx
    │   │   │   ├── showErrorToast.tsx
    │   │   │   ├── showSuccessToast.tsx
    │   │   │   └── showVersionUpdateToast.tsx
    │   │   ├── orderBy
    │   │   │   └── hooks
    │   │   │   │   ├── useOrderByState.clienttest.tsx
    │   │   │   │   └── useOrderByState.ts
    │   │   ├── organizations
    │   │   │   ├── components
    │   │   │   │   ├── DeleteOrganizationButton.tsx
    │   │   │   │   ├── NewOrganizationForm.tsx
    │   │   │   │   ├── ProjectOverview.tsx
    │   │   │   │   └── RenameOrganization.tsx
    │   │   │   ├── hooks.ts
    │   │   │   ├── server
    │   │   │   │   └── organizationRouter.ts
    │   │   │   └── utils
    │   │   │   │   └── organizationNameSchema.ts
    │   │   ├── otel
    │   │   │   └── server
    │   │   │   │   ├── OtelIngestionProcessor.ts
    │   │   │   │   └── attributes.ts
    │   │   ├── playground
    │   │   │   ├── page
    │   │   │   │   ├── components
    │   │   │   │   │   ├── CreateOrEditLLMSchemaDialog.tsx
    │   │   │   │   │   ├── CreateOrEditLLMToolDialog.tsx
    │   │   │   │   │   ├── GenerationOutput.tsx
    │   │   │   │   │   ├── JumpToPlaygroundButton.tsx
    │   │   │   │   │   ├── Messages.tsx
    │   │   │   │   │   ├── PlaygroundTools
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   ├── PromptVariableComponent.tsx
    │   │   │   │   │   ├── ResetPlaygroundButton.tsx
    │   │   │   │   │   ├── SaveToPromptButton.tsx
    │   │   │   │   │   ├── StructuredOutputSchemaSection.tsx
    │   │   │   │   │   └── Variables.tsx
    │   │   │   │   ├── context
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── hooks
    │   │   │   │   │   ├── useCommandEnter.ts
    │   │   │   │   │   ├── useModelParams.ts
    │   │   │   │   │   └── usePlaygroundCache.ts
    │   │   │   │   ├── index.tsx
    │   │   │   │   ├── playground.tsx
    │   │   │   │   └── types.ts
    │   │   │   └── server
    │   │   │   │   ├── analytics
    │   │   │   │       └── posthogCallback.ts
    │   │   │   │   ├── authorizeRequest.ts
    │   │   │   │   ├── chatCompletionHandler.ts
    │   │   │   │   └── validateChatCompletionBody.ts
    │   │   ├── posthog-analytics
    │   │   │   ├── ServerPosthog.ts
    │   │   │   └── usePostHogClientCapture.ts
    │   │   ├── posthog-integration
    │   │   │   ├── posthog-integration-router.ts
    │   │   │   └── types.ts
    │   │   ├── projects
    │   │   │   ├── components
    │   │   │   │   ├── ConfigureRetention.tsx
    │   │   │   │   ├── DeleteProjectButton.tsx
    │   │   │   │   ├── HostNameProject.tsx
    │   │   │   │   ├── NewProjectForm.tsx
    │   │   │   │   ├── RenameProject.tsx
    │   │   │   │   └── TransferProjectButton.tsx
    │   │   │   ├── hooks.ts
    │   │   │   └── server
    │   │   │   │   └── projectsRouter.ts
    │   │   ├── prompts
    │   │   │   ├── README.md
    │   │   │   ├── components
    │   │   │   │   ├── NewPromptForm
    │   │   │   │   │   ├── PromptChatMessages.tsx
    │   │   │   │   │   ├── ReviewPromptDialog.tsx
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   └── validation.ts
    │   │   │   │   ├── PromptSelectionDialog.tsx
    │   │   │   │   ├── PromptVariableListPreview.tsx
    │   │   │   │   ├── PromptVersionDiffDialog.tsx
    │   │   │   │   ├── ProtectedLabelsSettings.tsx
    │   │   │   │   ├── SetPromptVersionLabels
    │   │   │   │   │   ├── AddLabelForm.tsx
    │   │   │   │   │   ├── LabelCommandItem.tsx
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── auto-complete.tsx
    │   │   │   │   ├── delete-prompt-version.tsx
    │   │   │   │   ├── delete-prompt.tsx
    │   │   │   │   ├── duplicate-prompt.tsx
    │   │   │   │   ├── prompt-detail.tsx
    │   │   │   │   ├── prompt-history.tsx
    │   │   │   │   ├── prompt-new.tsx
    │   │   │   │   ├── prompts-table.tsx
    │   │   │   │   └── renderContentWithPromptButtons.tsx
    │   │   │   ├── constants.ts
    │   │   │   ├── hooks
    │   │   │   │   └── usePromptNameValidation.tsx
    │   │   │   ├── server
    │   │   │   │   ├── actions
    │   │   │   │   │   ├── createPrompt.ts
    │   │   │   │   │   ├── getPromptByName.ts
    │   │   │   │   │   ├── getPromptsMeta.ts
    │   │   │   │   │   └── updatePrompts.ts
    │   │   │   │   ├── handlers
    │   │   │   │   │   ├── promptNameHandler.ts
    │   │   │   │   │   ├── promptVersionHandler.ts
    │   │   │   │   │   └── promptsHandler.ts
    │   │   │   │   ├── routers
    │   │   │   │   │   └── promptRouter.ts
    │   │   │   │   └── utils
    │   │   │   │   │   ├── authorizePromptRequest.ts
    │   │   │   │   │   ├── checkHasProtectedLabels.ts
    │   │   │   │   │   ├── updatePromptLabels.ts
    │   │   │   │   │   ├── updatePromptTags.ts
    │   │   │   │   │   └── validation.ts
    │   │   │   └── utils.ts
    │   │   ├── public-api
    │   │   │   ├── README.md
    │   │   │   ├── components
    │   │   │   │   ├── ApiKeyList.tsx
    │   │   │   │   ├── CreateApiKeyButton.tsx
    │   │   │   │   ├── CreateLLMApiKeyDialog.tsx
    │   │   │   │   ├── CreateLLMApiKeyForm.tsx
    │   │   │   │   ├── LLMApiKeyList.tsx
    │   │   │   │   ├── QuickstartExamples.tsx
    │   │   │   │   └── UpdateLLMApiKeyDialog.tsx
    │   │   │   ├── server
    │   │   │   │   ├── RateLimitService.ts
    │   │   │   │   ├── apiAuth.ts
    │   │   │   │   ├── cors.ts
    │   │   │   │   ├── createAuthedProjectAPIRoute.ts
    │   │   │   │   ├── dailyMetrics.ts
    │   │   │   │   ├── filter-builder.ts
    │   │   │   │   ├── observations.ts
    │   │   │   │   ├── organizationApiKeyRouter.ts
    │   │   │   │   ├── projectApiKeyRouter.ts
    │   │   │   │   ├── scores-api-service.ts
    │   │   │   │   ├── scores.ts
    │   │   │   │   ├── traces.ts
    │   │   │   │   └── withMiddlewares.ts
    │   │   │   └── types
    │   │   │   │   ├── annotation-queues.ts
    │   │   │   │   ├── comments.ts
    │   │   │   │   ├── datasets.ts
    │   │   │   │   ├── events.ts
    │   │   │   │   ├── generations.ts
    │   │   │   │   ├── metrics.ts
    │   │   │   │   ├── models.ts
    │   │   │   │   ├── observations.ts
    │   │   │   │   ├── sessions.ts
    │   │   │   │   ├── spans.ts
    │   │   │   │   └── traces.ts
    │   │   ├── query
    │   │   │   ├── dashboardUiTableToViewMapping.ts
    │   │   │   ├── dataModel.ts
    │   │   │   ├── index.ts
    │   │   │   ├── server
    │   │   │   │   └── queryBuilder.ts
    │   │   │   └── types.ts
    │   │   ├── rbac
    │   │   │   ├── components
    │   │   │   │   ├── CreateProjectMemberButton.tsx
    │   │   │   │   ├── MembersTable.tsx
    │   │   │   │   ├── MembershipInvitesPage.tsx
    │   │   │   │   └── RoleSelectItem.tsx
    │   │   │   ├── constants
    │   │   │   │   ├── orderedRoles.ts
    │   │   │   │   ├── organizationAccessRights.ts
    │   │   │   │   └── projectAccessRights.ts
    │   │   │   ├── server
    │   │   │   │   ├── allInvitesRoutes.ts
    │   │   │   │   ├── allMembersRoutes.ts
    │   │   │   │   └── membersRouter.ts
    │   │   │   └── utils
    │   │   │   │   ├── checkOrganizationAccess.ts
    │   │   │   │   └── checkProjectAccess.ts
    │   │   ├── scores
    │   │   │   ├── adapters
    │   │   │   │   └── index.ts
    │   │   │   ├── components
    │   │   │   │   ├── AnnotateDrawer.tsx
    │   │   │   │   ├── AnnotateDrawerContent.tsx
    │   │   │   │   ├── CreateScoreConfigButton.tsx
    │   │   │   │   ├── ScoreChart.tsx
    │   │   │   │   ├── ScoreConfigDetails.tsx
    │   │   │   │   ├── ScoreConfigSettings.tsx
    │   │   │   │   ├── ScoreDetailColumnHelpers.tsx
    │   │   │   │   ├── TimeseriesChart.tsx
    │   │   │   │   └── multi-select-key-values.tsx
    │   │   │   ├── hooks
    │   │   │   │   ├── useIndividualScoreColumns.ts
    │   │   │   │   ├── useScoreCustomOptimistic.ts
    │   │   │   │   ├── useScoreMutations.ts
    │   │   │   │   └── useScoreValues.ts
    │   │   │   ├── lib
    │   │   │   │   ├── aggregateScores.ts
    │   │   │   │   ├── getDefaultScoreData.ts
    │   │   │   │   ├── helpers.ts
    │   │   │   │   └── types.ts
    │   │   │   ├── schema.ts
    │   │   │   └── types.ts
    │   │   ├── setup
    │   │   │   ├── components
    │   │   │   │   ├── SetupPage.tsx
    │   │   │   │   └── SetupTracingButton.tsx
    │   │   │   └── setupRoutes.ts
    │   │   ├── slack
    │   │   │   └── server
    │   │   │   │   └── slack-webhook.ts
    │   │   ├── support-chat
    │   │   │   ├── PlainChat.tsx
    │   │   │   ├── createSupportEmailHash.ts
    │   │   │   └── trpc
    │   │   │   │   └── plain.ts
    │   │   ├── table
    │   │   │   ├── components
    │   │   │   │   ├── TableActionDialog.tsx
    │   │   │   │   ├── TableActionMenu.tsx
    │   │   │   │   ├── TableActionTargetOptions.tsx
    │   │   │   │   ├── TableSelectionManager.tsx
    │   │   │   │   └── targetOptionsQueryMap.tsx
    │   │   │   ├── hooks
    │   │   │   │   └── useSelectAll.ts
    │   │   │   ├── server
    │   │   │   │   ├── createBatchActionJob.ts
    │   │   │   │   ├── helpers.ts
    │   │   │   │   └── tableRouter.ts
    │   │   │   └── types.ts
    │   │   ├── tag
    │   │   │   ├── components
    │   │   │   │   ├── TagButton.tsx
    │   │   │   │   ├── TagCommandItem.tsx
    │   │   │   │   ├── TagCreateItem.tsx
    │   │   │   │   ├── TagInput.tsx
    │   │   │   │   ├── TagList.tsx
    │   │   │   │   ├── TagMananger.tsx
    │   │   │   │   ├── TagPromptDetailsPopover.tsx
    │   │   │   │   ├── TagPromptPopover.tsx
    │   │   │   │   ├── TagTraceDetailsPopover.tsx
    │   │   │   │   └── TagTracePopver.tsx
    │   │   │   └── hooks
    │   │   │   │   └── useTagManager.tsx
    │   │   ├── telemetry
    │   │   │   ├── README.md
    │   │   │   └── index.ts
    │   │   ├── theming
    │   │   │   ├── ThemeProvider.tsx
    │   │   │   ├── ThemeToggle.tsx
    │   │   │   └── useMarkdownContext.tsx
    │   │   ├── trace-graph-view
    │   │   │   ├── components
    │   │   │   │   ├── TraceGraphCanvas.tsx
    │   │   │   │   └── TraceGraphView.tsx
    │   │   │   └── types.ts
    │   │   └── widgets
    │   │   │   ├── chart-library
    │   │   │       ├── BigNumber.tsx
    │   │   │       ├── Chart.tsx
    │   │   │       ├── HistogramChart.tsx
    │   │   │       ├── HorizontalBarChart.tsx
    │   │   │       ├── LineChartTimeSeries.tsx
    │   │   │       ├── PieChart.tsx
    │   │   │       ├── VerticalBarChart.tsx
    │   │   │       ├── VerticalBarChartTimeSeries.tsx
    │   │   │       ├── chart-props.ts
    │   │   │       └── utils.ts
    │   │   │   ├── components
    │   │   │       ├── DashboardGrid.tsx
    │   │   │       ├── DashboardWidget.tsx
    │   │   │       ├── SelectWidgetDialog.tsx
    │   │   │       ├── WidgetForm.tsx
    │   │   │       ├── WidgetPropertySelectItem.tsx
    │   │   │       └── WidgetTable.tsx
    │   │   │   ├── index.ts
    │   │   │   └── utils.ts
    │   ├── hooks
    │   │   ├── use-element-visibility.tsx
    │   │   ├── use-environment-filter.tsx
    │   │   ├── use-mobile.tsx
    │   │   ├── useDashboardDateRange.tsx
    │   │   ├── useDebounce.tsx
    │   │   ├── useProjectIdFromURL.ts
    │   │   ├── useTableDateRange.tsx
    │   │   └── useUniqueNameValidation.tsx
    │   ├── initialize.ts
    │   ├── instrumentation.ts
    │   ├── observability.config.ts
    │   ├── pages
    │   │   ├── _app.tsx
    │   │   ├── api
    │   │   │   ├── admin
    │   │   │   │   ├── api-keys
    │   │   │   │   │   └── index.ts
    │   │   │   │   ├── bullmq
    │   │   │   │   │   └── index.ts
    │   │   │   │   └── organizations
    │   │   │   │   │   ├── [organizationId]
    │   │   │   │   │       ├── apiKeys
    │   │   │   │   │       │   ├── [apiKeyId].ts
    │   │   │   │   │       │   └── index.ts
    │   │   │   │   │       └── index.ts
    │   │   │   │   │   └── index.ts
    │   │   │   ├── auth
    │   │   │   │   ├── [...nextauth].ts
    │   │   │   │   ├── add-sso-config.ts
    │   │   │   │   ├── check-sso.ts
    │   │   │   │   └── signup.ts
    │   │   │   ├── billing
    │   │   │   │   └── README.md
    │   │   │   ├── feedback.ts
    │   │   │   ├── public
    │   │   │   │   ├── annotation-queues
    │   │   │   │   │   ├── [queueId].ts
    │   │   │   │   │   ├── [queueId]
    │   │   │   │   │   │   └── items
    │   │   │   │   │   │   │   ├── [itemId].ts
    │   │   │   │   │   │   │   └── index.ts
    │   │   │   │   │   └── index.ts
    │   │   │   │   ├── comments
    │   │   │   │   │   ├── [commentId].ts
    │   │   │   │   │   └── index.ts
    │   │   │   │   ├── dataset-items
    │   │   │   │   │   ├── [datasetItemId].ts
    │   │   │   │   │   └── index.ts
    │   │   │   │   ├── dataset-run-items.ts
    │   │   │   │   ├── datasets.ts
    │   │   │   │   ├── datasets
    │   │   │   │   │   └── [name]
    │   │   │   │   │   │   ├── index.ts
    │   │   │   │   │   │   └── runs
    │   │   │   │   │   │       ├── [runName].ts
    │   │   │   │   │   │       └── index.ts
    │   │   │   │   ├── events.ts
    │   │   │   │   ├── generations.ts
    │   │   │   │   ├── health.ts
    │   │   │   │   ├── ingestion.ts
    │   │   │   │   ├── media
    │   │   │   │   │   ├── [mediaId].ts
    │   │   │   │   │   └── index.ts
    │   │   │   │   ├── metrics
    │   │   │   │   │   ├── daily.ts
    │   │   │   │   │   └── index.ts
    │   │   │   │   ├── models
    │   │   │   │   │   ├── [modelId]
    │   │   │   │   │   │   └── index.ts
    │   │   │   │   │   └── index.ts
    │   │   │   │   ├── observations
    │   │   │   │   │   ├── [observationId].ts
    │   │   │   │   │   └── index.ts
    │   │   │   │   ├── organizations
    │   │   │   │   │   ├── memberships
    │   │   │   │   │   │   └── index.ts
    │   │   │   │   │   └── projects
    │   │   │   │   │   │   └── index.ts
    │   │   │   │   ├── otel
    │   │   │   │   │   ├── otlp-proto
    │   │   │   │   │   │   ├── README.md
    │   │   │   │   │   │   └── generated
    │   │   │   │   │   │   │   └── root.ts
    │   │   │   │   │   └── v1
    │   │   │   │   │   │   ├── metrics
    │   │   │   │   │   │       └── index.ts
    │   │   │   │   │   │   └── traces
    │   │   │   │   │   │       └── index.ts
    │   │   │   │   ├── projects
    │   │   │   │   │   ├── [projectId]
    │   │   │   │   │   │   ├── apiKeys
    │   │   │   │   │   │   │   ├── [apiKeyId].ts
    │   │   │   │   │   │   │   └── index.ts
    │   │   │   │   │   │   ├── index.ts
    │   │   │   │   │   │   └── memberships
    │   │   │   │   │   │   │   └── index.ts
    │   │   │   │   │   └── index.ts
    │   │   │   │   ├── prompts.ts
    │   │   │   │   ├── ready.ts
    │   │   │   │   ├── scim
    │   │   │   │   │   ├── ResourceTypes.ts
    │   │   │   │   │   ├── Schemas.ts
    │   │   │   │   │   ├── ServiceProviderConfig.ts
    │   │   │   │   │   └── Users
    │   │   │   │   │   │   ├── [id].ts
    │   │   │   │   │   │   └── index.ts
    │   │   │   │   ├── score-configs
    │   │   │   │   │   ├── [configId].ts
    │   │   │   │   │   └── index.ts
    │   │   │   │   ├── scores
    │   │   │   │   │   ├── [scoreId].ts
    │   │   │   │   │   └── index.ts
    │   │   │   │   ├── sessions
    │   │   │   │   │   ├── [sessionId].ts
    │   │   │   │   │   └── index.ts
    │   │   │   │   ├── spans.ts
    │   │   │   │   ├── traces
    │   │   │   │   │   ├── [traceId].ts
    │   │   │   │   │   └── index.ts
    │   │   │   │   └── v2
    │   │   │   │   │   ├── datasets
    │   │   │   │   │       ├── [datasetName]
    │   │   │   │   │       │   └── index.ts
    │   │   │   │   │       └── index.ts
    │   │   │   │   │   ├── prompts
    │   │   │   │   │       ├── [promptName]
    │   │   │   │   │       │   ├── index.ts
    │   │   │   │   │       │   └── versions
    │   │   │   │   │       │   │   └── [promptVersion].ts
    │   │   │   │   │       └── index.ts
    │   │   │   │   │   └── scores
    │   │   │   │   │       ├── [scoreId].ts
    │   │   │   │   │       └── index.ts
    │   │   │   └── trpc
    │   │   │   │   └── [trpc].ts
    │   │   ├── auth
    │   │   │   ├── error.tsx
    │   │   │   ├── hf-spaces.tsx
    │   │   │   ├── reset-password.tsx
    │   │   │   ├── sign-in.tsx
    │   │   │   └── sign-up.tsx
    │   │   ├── background-migrations.tsx
    │   │   ├── index.tsx
    │   │   ├── onboarding.tsx
    │   │   ├── organization
    │   │   │   └── [organizationId]
    │   │   │   │   ├── index.tsx
    │   │   │   │   ├── settings
    │   │   │   │       ├── [page].tsx
    │   │   │   │       └── index.tsx
    │   │   │   │   └── setup.tsx
    │   │   ├── project
    │   │   │   └── [projectId]
    │   │   │   │   ├── annotation-queues.tsx
    │   │   │   │   ├── annotation-queues
    │   │   │   │       └── [queueId]
    │   │   │   │       │   ├── index.tsx
    │   │   │   │       │   └── items
    │   │   │   │       │       ├── [itemId].tsx
    │   │   │   │       │       └── index.tsx
    │   │   │   │   ├── dashboards
    │   │   │   │       ├── [dashboardId]
    │   │   │   │       │   └── index.tsx
    │   │   │   │       ├── index.tsx
    │   │   │   │       └── new.tsx
    │   │   │   │   ├── datasets.tsx
    │   │   │   │   ├── datasets
    │   │   │   │       └── [datasetId]
    │   │   │   │       │   ├── compare.tsx
    │   │   │   │       │   ├── index.tsx
    │   │   │   │       │   ├── items.tsx
    │   │   │   │       │   ├── items
    │   │   │   │       │       └── [itemId].tsx
    │   │   │   │       │   └── runs
    │   │   │   │       │       └── [runId].tsx
    │   │   │   │   ├── evals
    │   │   │   │       ├── [evaluatorId].tsx
    │   │   │   │       ├── configs
    │   │   │   │       │   ├── [configId].tsx
    │   │   │   │       │   ├── index.tsx
    │   │   │   │       │   └── new.tsx
    │   │   │   │       ├── default-model.tsx
    │   │   │   │       ├── index.tsx
    │   │   │   │       ├── new.tsx
    │   │   │   │       └── templates
    │   │   │   │       │   ├── [id].tsx
    │   │   │   │       │   ├── index.tsx
    │   │   │   │       │   └── new.tsx
    │   │   │   │   ├── index.tsx
    │   │   │   │   ├── models.tsx
    │   │   │   │   ├── observations.tsx
    │   │   │   │   ├── playground.tsx
    │   │   │   │   ├── prompts
    │   │   │   │       ├── [promptName]
    │   │   │   │       │   ├── index.tsx
    │   │   │   │       │   └── metrics.tsx
    │   │   │   │       ├── index.tsx
    │   │   │   │       └── new.tsx
    │   │   │   │   ├── scores.tsx
    │   │   │   │   ├── sessions.tsx
    │   │   │   │   ├── sessions
    │   │   │   │       └── [sessionId].tsx
    │   │   │   │   ├── settings
    │   │   │   │       ├── [page].tsx
    │   │   │   │       ├── billing.ts
    │   │   │   │       ├── index.tsx
    │   │   │   │       ├── integrations
    │   │   │   │       │   ├── blobstorage.tsx
    │   │   │   │       │   └── posthog.tsx
    │   │   │   │       └── models
    │   │   │   │       │   └── [modelId].tsx
    │   │   │   │   ├── setup.tsx
    │   │   │   │   ├── traces.tsx
    │   │   │   │   ├── traces
    │   │   │   │       └── [traceId].tsx
    │   │   │   │   ├── users.tsx
    │   │   │   │   ├── users
    │   │   │   │       └── [userId].tsx
    │   │   │   │   └── widgets
    │   │   │   │       ├── [widgetId]
    │   │   │   │           └── index.tsx
    │   │   │   │       ├── index.tsx
    │   │   │   │       └── new.tsx
    │   │   ├── public
    │   │   │   └── traces
    │   │   │   │   └── [traceId].tsx
    │   │   ├── setup.tsx
    │   │   └── trace
    │   │   │   └── [traceId].tsx
    │   ├── server
    │   │   ├── api
    │   │   │   ├── definitions
    │   │   │   │   ├── evalConfigsTable.ts
    │   │   │   │   ├── evalExecutionsTable.ts
    │   │   │   │   ├── promptsTable.ts
    │   │   │   │   ├── scoresTable.ts
    │   │   │   │   └── usersTable.ts
    │   │   │   ├── root.ts
    │   │   │   ├── routers
    │   │   │   │   ├── auditLogs.ts
    │   │   │   │   ├── comments.ts
    │   │   │   │   ├── dashboardWidgets.ts
    │   │   │   │   ├── generations
    │   │   │   │   │   ├── db
    │   │   │   │   │   │   └── getAllGenerationsSqlQuery.ts
    │   │   │   │   │   ├── filterOptionsQuery.ts
    │   │   │   │   │   ├── getAllQueries.ts
    │   │   │   │   │   ├── index.ts
    │   │   │   │   │   └── utils
    │   │   │   │   │   │   └── GenerationTableOptions.ts
    │   │   │   │   ├── media.ts
    │   │   │   │   ├── models.ts
    │   │   │   │   ├── observations.ts
    │   │   │   │   ├── public.ts
    │   │   │   │   ├── scoreConfigs.ts
    │   │   │   │   ├── scores.ts
    │   │   │   │   ├── sessions.ts
    │   │   │   │   ├── tableViewPresets.ts
    │   │   │   │   ├── traces.ts
    │   │   │   │   ├── users.ts
    │   │   │   │   └── utilities.ts
    │   │   │   ├── services
    │   │   │   │   ├── sqlInterface.ts
    │   │   │   │   └── tableDefinitions.ts
    │   │   │   └── trpc.ts
    │   │   ├── auth.ts
    │   │   ├── db.ts
    │   │   └── utils
    │   │   │   ├── checkProjectMembershipOrAdmin.ts
    │   │   │   └── cookies.ts
    │   ├── styles
    │   │   └── globals.css
    │   └── utils
    │   │   ├── api.ts
    │   │   ├── clipboard.ts
    │   │   ├── date-range-utils.ts
    │   │   ├── dates.ts
    │   │   ├── exceptions.ts
    │   │   ├── getFinalModelParams.tsx
    │   │   ├── numbers.ts
    │   │   ├── shutdown.ts
    │   │   ├── string.ts
    │   │   ├── superjson.ts
    │   │   ├── tailwind.ts
    │   │   ├── tanstack.d.ts
    │   │   ├── trpcErrorToast.tsx
    │   │   └── types.ts
    ├── tailwind.config.ts
    ├── tsconfig.json
    └── types
    │   ├── global.d.ts
    │   └── next-auth.d.ts
└── worker
    ├── .eslintrc.js
    ├── Dockerfile
    ├── entrypoint.sh
    ├── package.json
    ├── src
        ├── __tests__
        │   ├── batchAction.test.ts
        │   ├── batchExport.test.ts
        │   ├── blobStorageIntegrationProcessing.test.ts
        │   ├── dataRetentionProcessing.test.ts
        │   ├── evalService.filtering.test.ts
        │   ├── evalService.test.ts
        │   ├── experimentsService.test.ts
        │   ├── modelMatch.test.ts
        │   ├── network.ts
        │   ├── projectDeletionProcessing.test.ts
        │   ├── redisConsumer.test.ts
        │   ├── scoreDeletion.test.ts
        │   ├── storageservice.test.ts
        │   ├── traceDeletion.test.ts
        │   └── utils.ts
        ├── api
        │   └── index.ts
        ├── app.ts
        ├── backgroundMigrations
        │   ├── IBackgroundMigration.ts
        │   ├── README.md
        │   ├── addGenerationsCostBackfill.ts
        │   ├── backgroundMigrationManager.ts
        │   ├── migrateEventLogToBlobStorageRefTable.ts
        │   ├── migrateObservationsFromPostgresToClickhouse.ts
        │   ├── migrateScoresFromPostgresToClickhouse.ts
        │   └── migrateTracesFromPostgresToClickhouse.ts
        ├── constants
        │   ├── VERSION.ts
        │   ├── default-model-prices.json
        │   ├── langfuse-dashboards.json
        │   └── managed-evaluators.json
        ├── database.ts
        ├── ee
        │   ├── cloudUsageMetering
        │   │   ├── constants.ts
        │   │   └── handleCloudUsageMeteringJob.ts
        │   ├── dataRetention
        │   │   ├── handleDataRetentionProcessingJob.ts
        │   │   └── handleDataRetentionSchedule.ts
        │   └── meteringDataPostgresExport
        │   │   └── handleMeteringDataPostgresExportJob.ts
        ├── env.ts
        ├── features
        │   ├── batchAction
        │   │   ├── handleBatchActionJob.ts
        │   │   └── processAddToQueue.ts
        │   ├── batchExport
        │   │   └── handleBatchExportJob.ts
        │   ├── blobstorage
        │   │   ├── handleBlobStorageIntegrationProjectJob.ts
        │   │   └── handleBlobStorageIntegrationSchedule.ts
        │   ├── database-read-stream
        │   │   ├── getDatabaseReadStream.ts
        │   │   └── types.ts
        │   ├── evaluation
        │   │   └── evalService.ts
        │   ├── experiments
        │   │   └── experimentService.ts
        │   ├── health
        │   │   └── index.ts
        │   ├── posthog
        │   │   ├── handlePostHogIntegrationProjectJob.ts
        │   │   └── handlePostHogIntegrationSchedule.ts
        │   ├── scores
        │   │   └── processClickhouseScoreDelete.ts
        │   ├── tokenisation
        │   │   ├── types.ts
        │   │   └── usage.ts
        │   ├── traces
        │   │   ├── processClickhouseTraceDelete.ts
        │   │   └── processPostgresTraceDelete.ts
        │   └── utilities.ts
        ├── index.ts
        ├── initialize.ts
        ├── instrumentation.ts
        ├── interfaces
        │   ├── ErrorResponse.ts
        │   └── MessageResponse.ts
        ├── middlewares.ts
        ├── queues
        │   ├── batchActionQueue.ts
        │   ├── batchExportQueue.ts
        │   ├── blobStorageIntegrationQueue.ts
        │   ├── cloudUsageMeteringQueue.ts
        │   ├── coreDataS3ExportQueue.ts
        │   ├── dataRetentionQueue.ts
        │   ├── evalQueue.ts
        │   ├── experimentQueue.ts
        │   ├── ingestionQueue.ts
        │   ├── postHogIntegrationQueue.ts
        │   ├── projectDelete.ts
        │   ├── scoreDelete.ts
        │   ├── traceDelete.ts
        │   └── workerManager.ts
        ├── scripts
        │   ├── createDefaultModelPricesJson.ts
        │   ├── refill-billing-event.ts
        │   ├── s3-ingestion-event-relpay.ts
        │   ├── upsertDefaultModelPrices.ts
        │   ├── upsertLangfuseDashboards.ts
        │   ├── upsertManagedEvaluators.ts
        │   └── verifyClickhouseRecords
        │   │   ├── README.md
        │   │   └── index.ts
        ├── services
        │   ├── ClickhouseWriter
        │   │   ├── ClickhouseWriter.unit.test.ts
        │   │   └── index.ts
        │   ├── IngestionService
        │   │   ├── index.ts
        │   │   ├── tests
        │   │   │   ├── IngestionService.integration.test.ts
        │   │   │   ├── IngestionService.unit.test.ts
        │   │   │   ├── calculateTokenCost.unit.test.ts
        │   │   │   └── utils.unit.test.ts
        │   │   └── utils.ts
        │   ├── dlq
        │   │   └── dlqRetryService.ts
        │   └── modelMatch.ts
        └── utils
        │   └── shutdown.ts
    └── tsconfig.json


/.codespellrc:
--------------------------------------------------------------------------------
1 | [codespell]
2 | skip = .git,*.pdf,*.svg,package-lock.json,*.prisma,pnpm-lock.yaml
3 | ignore-words-list = afterall,vertx,notIn
4 | 
5 | 


--------------------------------------------------------------------------------
/.cursor/environment.json:
--------------------------------------------------------------------------------
1 | {
2 |   "install": "cp .env.dev.example .env && pnpm i",
3 |   "build": {
4 |     "context": ".",
5 |     "dockerfile": "Dockerfile"
6 |   },
7 |   "start": "pnpm dx-f"
8 | }
9 | 


--------------------------------------------------------------------------------
/.cursor/rules/authorization-and-rbac.mdc:
--------------------------------------------------------------------------------
1 | ---
2 | description: How to manage authorization and RBAC within full-stack langfuse features
3 | globs: web/
4 | alwaysApply: true
5 | ---
6 | See [README.md](mdc:web/src/features/rbac/README.md) for details


--------------------------------------------------------------------------------
/.cursor/rules/entitlements.mdc:
--------------------------------------------------------------------------------
1 | ---
2 | description: How to enforce entitlements across full-stack features
3 | globs: web/**
4 | alwaysApply: true
5 | ---
6 | 
7 | Check [README.md](mdc:web/src/features/entitlements/README.md) to learn more about entitlements
8 | 


--------------------------------------------------------------------------------
/.cursor/rules/general-info.mdc:
--------------------------------------------------------------------------------
1 | ---
2 | description: 
3 | globs: 
4 | alwaysApply: true
5 | ---
6 | # General rules
7 | 
8 | - Linting in this repo only works if the development server is running


--------------------------------------------------------------------------------
/.dockerignore:
--------------------------------------------------------------------------------
1 | Dockerfile
2 | .dockerignore
3 | node_modules
4 | npm-debug.log
5 | README.md
6 | **/.next
7 | .git
8 | **/node_modules


--------------------------------------------------------------------------------
/.eslintignore:
--------------------------------------------------------------------------------
1 | node_modules
2 | **/node_modules
3 | build
4 | coverage


--------------------------------------------------------------------------------
/.github/CODEOWNERS:
--------------------------------------------------------------------------------
1 | # Currently inactive
2 | # * @langfuse/maintainers
3 | 


--------------------------------------------------------------------------------
/.github/DISCUSSION_TEMPLATE/ideas.yml:
--------------------------------------------------------------------------------
 1 | body:
 2 |   - type: textarea
 3 |     attributes:
 4 |       label: Describe the feature or potential improvement
 5 |       description: Please describe the change as clear and concise as possible. Remember to add context as to why you believe this is needed.
 6 |     validations:
 7 |       required: true
 8 |   - type: textarea
 9 |     attributes:
10 |       label: Additional information
11 |       description: Add any other information related to the change here. If your idea is related to any issues or discussions, link them here.
12 | 


--------------------------------------------------------------------------------
/.github/ISSUE_TEMPLATE/config.yml:
--------------------------------------------------------------------------------
1 | contact_links:
2 |   - name: 💡 Feature Request
3 |     url: https://github.com/orgs/langfuse/discussions/new?category=ideas
4 |     about: Suggest any ideas you have using our discussion forums.
5 |   - name: 🤗 Get Help
6 |     url: https://github.com/orgs/langfuse/discussions/new?category=support
7 |     about: If you can’t get something to work the way you expect, open a question in our discussion forums.
8 | 


--------------------------------------------------------------------------------
/.github/workflows/codespell.yml:
--------------------------------------------------------------------------------
 1 | ---
 2 | name: Codespell
 3 | 
 4 | on:
 5 |   push:
 6 |     branches:
 7 |       - "main"
 8 |     tags:
 9 |       - "v*"
10 |   pull_request:
11 |     branches:
12 |       - "**"
13 |   merge_group:
14 | 
15 | permissions:
16 |   contents: read
17 | 
18 | jobs:
19 |   codespell:
20 |     name: Check for spelling errors
21 |     runs-on: ubuntu-latest
22 | 
23 |     steps:
24 |       - name: Checkout
25 |         uses: actions/checkout@v3
26 |       - name: Codespell
27 |         uses: codespell-project/actions-codespell@v2
28 | 


--------------------------------------------------------------------------------
/.github/workflows/dependabot-rebase-stale.yml:
--------------------------------------------------------------------------------
 1 | name: Rebase Dependabot stale PRs
 2 | 
 3 | on:
 4 |   push:
 5 |     branches:
 6 |       - main
 7 |   workflow_dispatch:
 8 | 
 9 | jobs:
10 |   rebase-dependabot:
11 |     runs-on: ubuntu-latest
12 |     environment: "protected branches"
13 |     steps:
14 |       - name: "Rebase open Dependabot PR"
15 |         uses: orange-buffalo/dependabot-auto-rebase@v1
16 |         with:
17 |           api-token: ${{ secrets.GH_ACCESS_TOKEN }}
18 |           repository: ${{ github.repository }}
19 | 


--------------------------------------------------------------------------------
/.github/workflows/release.yml:
--------------------------------------------------------------------------------
 1 | on:
 2 |   workflow_dispatch:
 3 |   push:
 4 |     # Pattern matched against refs/tags
 5 |     tags:
 6 |       - "v3.[0-9]+.[0-9]+" # Semantic version tags
 7 | 
 8 | jobs:
 9 |   release:
10 |     runs-on: ubuntu-latest
11 |     environment: "protected branches"
12 |     steps:
13 |       - uses: actions/checkout@v4
14 |         with:
15 |           ref: main # Always checkout main even for tagged releases
16 |           fetch-depth: 0
17 |           token: ${{ secrets.GH_ACCESS_TOKEN }}
18 |       - name: Push to production
19 |         run: git push origin +main:production
20 | 


--------------------------------------------------------------------------------
/.npmrc:
--------------------------------------------------------------------------------
1 | public-hoist-pattern[]=*prisma*


--------------------------------------------------------------------------------
/.nvmrc:
--------------------------------------------------------------------------------
1 | v20


--------------------------------------------------------------------------------
/.vscode/extensions.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "recommendations": [
 3 |     "esbenp.prettier-vscode",
 4 |     "dbaeumer.vscode-eslint",
 5 |     "bradlc.vscode-tailwindcss",
 6 |     "unifiedjs.vscode-mdx",
 7 |     "yoavbls.pretty-ts-errors",
 8 |     "Prisma.prisma"
 9 |   ]
10 | }
11 | 


--------------------------------------------------------------------------------
/AGENTS.md:
--------------------------------------------------------------------------------
 1 | # Codex Guidelines for Langfuse
 2 | 
 3 | Langfuse is an **open source LLM engineering** platform for developing, monitoring, evaluating and debugging AI applications. See the README for more details.
 4 | 
 5 | ## Linting
 6 | - Run `pnpm run lint` to lint all packages.
 7 | - Fix issues automatically with `pnpm run lint:fix`.
 8 | 
 9 | ## Tests
10 | - Codex cannot run the test suite because it depends on Docker-based infrastructure that is unavailable in this environment.
11 | 
12 | ## Cursor Rules
13 | - Additional folder-specific rules live in `.cursor/rules/`.
14 | 
15 | ## Commits
16 | - Follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) when crafting commit messages.
17 | 


--------------------------------------------------------------------------------
/SECURITY.md:
--------------------------------------------------------------------------------
1 | ## Security Policy
2 | We strongly recommend using the latest version of Langfuse to receive all security updates.
3 | 
4 | For more information, please refer to the [Data Security & Privacy](https://langfuse.com/docs/data-security-privacy) page in the documentation or contact security@langfuse.com.
5 | 


--------------------------------------------------------------------------------
/ee/.eslintrc.js:
--------------------------------------------------------------------------------
1 | /** @type {import("eslint").Linter.Config} */
2 | module.exports = {
3 |   extends: ["@repo/eslint-config/library.js"],
4 |   parser: "@typescript-eslint/parser",
5 |   parserOptions: {
6 |     project: true,
7 |   },
8 | };
9 | 


--------------------------------------------------------------------------------
/ee/README.md:
--------------------------------------------------------------------------------
1 | # Enterprise Edition
2 | 
3 | This folder includes features that are only available in the Enterprise Edition of Langfuse and on Langfuse Cloud.
4 | 
5 | See [LICENSE](../LICENSE) and [docs](https://langfuse.com/docs/open-source) for more details.
6 | 


--------------------------------------------------------------------------------
/ee/src/ee-license-check/index.ts:
--------------------------------------------------------------------------------
1 | import { env } from "../env";
2 | 
3 | export const isEeAvailable: boolean =
4 |   env.NEXT_PUBLIC_LANGFUSE_CLOUD_REGION !== undefined ||
5 |   env.LANGFUSE_EE_LICENSE_KEY !== undefined;
6 | 


--------------------------------------------------------------------------------
/ee/src/env.ts:
--------------------------------------------------------------------------------
 1 | import { z } from "zod/v4";
 2 | import { removeEmptyEnvVariables } from "@langfuse/shared";
 3 | 
 4 | const EnvSchema = z.object({
 5 |   NEXT_PUBLIC_LANGFUSE_CLOUD_REGION: z.string().optional(),
 6 |   LANGFUSE_EE_LICENSE_KEY: z.string().optional(),
 7 | });
 8 | 
 9 | export const env = EnvSchema.parse(removeEmptyEnvVariables(process.env));
10 | 


--------------------------------------------------------------------------------
/ee/src/index.ts:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langfuse/langfuse/c8b282dc822c8cec556663f25a000eee58c0dbf6/ee/src/index.ts


--------------------------------------------------------------------------------
/ee/tsconfig.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "extends": "@repo/typescript-config/base.json",
 3 |   "compilerOptions": {
 4 |     "moduleResolution": "NodeNext",
 5 |     "module": "NodeNext",
 6 |     "lib": ["ES2020"],
 7 |     "outDir": "./dist",
 8 |     "types": ["node"],
 9 |     "target": "ES2020",
10 |     "rootDir": "."
11 |   },
12 |   "include": ["."],
13 |   "exclude": ["node_modules", "dist"]
14 | }
15 | 


--------------------------------------------------------------------------------
/fern/apis/client/definition/api.yml:
--------------------------------------------------------------------------------
 1 | name: langfuse
 2 | error-discrimination:
 3 |   strategy: status-code
 4 | auth: bearer
 5 | imports:
 6 |   commons: commons.yml
 7 | errors:
 8 |   - commons.Error
 9 |   - commons.UnauthorizedError
10 |   - commons.AccessDeniedError
11 |   - commons.MethodNotAllowedError
12 | 


--------------------------------------------------------------------------------
/fern/apis/client/definition/commons.yml:
--------------------------------------------------------------------------------
 1 | errors:
 2 |   Error:
 3 |     status-code: 400
 4 |     type: string
 5 |   UnauthorizedError:
 6 |     status-code: 401
 7 |     type: string
 8 |   AccessDeniedError:
 9 |     status-code: 403
10 |     type: string
11 |   MethodNotAllowedError:
12 |     status-code: 405
13 |     type: string
14 | 


--------------------------------------------------------------------------------
/fern/apis/organizations/definition/commons.yml:
--------------------------------------------------------------------------------
 1 | errors:
 2 |   Error:
 3 |     status-code: 400
 4 |     type: string
 5 |   UnauthorizedError:
 6 |     status-code: 401
 7 |     type: string
 8 |   AccessDeniedError:
 9 |     status-code: 403
10 |     type: string
11 |   MethodNotAllowedError:
12 |     status-code: 405
13 |     type: string
14 | 


--------------------------------------------------------------------------------
/fern/apis/organizations/generators.yml:
--------------------------------------------------------------------------------
 1 | default-group: local
 2 | groups:
 3 |   local:
 4 |     generators:
 5 |       - name: fernapi/fern-openapi
 6 |         version: 0.1.7
 7 |         output:
 8 |           location: local-file-system
 9 |           path: ../../../web/public/generated/organizations-api
10 |         config:
11 |           namespaceExport: Langfuse
12 |           allowCustomFetcher: true
13 |       - name: fernapi/fern-postman
14 |         version: 0.0.45
15 |         output:
16 |           location: local-file-system
17 |           path: ../../../web/public/generated/organizations-postman
18 | 


--------------------------------------------------------------------------------
/fern/fern.config.json:
--------------------------------------------------------------------------------
1 | {
2 |   "organization": "langfuse",
3 |   "version": "0.56.0"
4 | }
5 | 


--------------------------------------------------------------------------------
/generated/.gitignore:
--------------------------------------------------------------------------------
1 | python/


--------------------------------------------------------------------------------
/packages/config-eslint/package.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "name": "@repo/eslint-config",
 3 |   "version": "0.0.0",
 4 |   "license": "MIT",
 5 |   "private": true,
 6 |   "files": [
 7 |     "library.js",
 8 |     "next.js"
 9 |   ],
10 |   "devDependencies": {
11 |     "@typescript-eslint/eslint-plugin": "^7.1.0",
12 |     "@typescript-eslint/parser": "^7.12.0",
13 |     "@vercel/style-guide": "^6.0.0",
14 |     "eslint-config-next": "^14.2.15",
15 |     "eslint-config-prettier": "^9.1.0",
16 |     "eslint-config-turbo": "^1.13.4",
17 |     "eslint-plugin-only-warn": "^1.1.0",
18 |     "typescript": "^5.4.5"
19 |   }
20 | }
21 | 


--------------------------------------------------------------------------------
/packages/config-typescript/base.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "$schema": "https://json.schemastore.org/tsconfig",
 3 |   "display": "Default",
 4 |   "compilerOptions": {
 5 |     "composite": false,
 6 |     "declaration": true,
 7 |     "declarationMap": true,
 8 |     "esModuleInterop": true,
 9 |     "forceConsistentCasingInFileNames": true,
10 |     "inlineSources": false,
11 |     "isolatedModules": true,
12 |     "module": "ESNext",
13 |     "noErrorTruncation": true,
14 |     "moduleResolution": "Bundler",
15 |     "noUnusedLocals": false,
16 |     "noUnusedParameters": false,
17 |     "preserveWatchOutput": true,
18 |     "skipLibCheck": true,
19 |     "strict": true
20 |   },
21 |   "exclude": ["node_modules"]
22 | }
23 | 


--------------------------------------------------------------------------------
/packages/config-typescript/package.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "name": "@repo/typescript-config",
 3 |   "license": "MIT",
 4 |   "version": "0.0.0",
 5 |   "private": true,
 6 |   "publishConfig": {
 7 |     "access": "public"
 8 |   }
 9 | }
10 | 


--------------------------------------------------------------------------------
/packages/shared/.eslintrc.js:
--------------------------------------------------------------------------------
1 | /** @type {import("eslint").Linter.Config} */
2 | module.exports = {
3 |   extends: ["@repo/eslint-config/library.js"],
4 |   parser: "@typescript-eslint/parser",
5 |   parserOptions: {
6 |     project: true,
7 |   },
8 | };
9 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0001_traces.down.sql:
--------------------------------------------------------------------------------
1 | DROP TABLE traces ON CLUSTER default;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0002_observations.down.sql:
--------------------------------------------------------------------------------
1 | DROP TABLE observations ON CLUSTER default;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0003_scores.down.sql:
--------------------------------------------------------------------------------
1 | DROP TABLE scores ON CLUSTER default;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0004_drop_observations_index.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE observations ON CLUSTER default ADD INDEX IF NOT EXISTS idx_project_id project_id TYPE bloom_filter() GRANULARITY 1;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0004_drop_observations_index.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE observations ON CLUSTER default DROP INDEX IF EXISTS idx_project_id;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0005_add_session_id_index.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE traces ON CLUSTER default DROP INDEX IF EXISTS idx_session_id;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0005_add_session_id_index.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE traces ON CLUSTER default ADD INDEX IF NOT EXISTS idx_session_id session_id TYPE bloom_filter() GRANULARITY 1;
2 | ALTER TABLE traces ON CLUSTER default MATERIALIZE INDEX IF EXISTS idx_session_id;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0006_add_user_id_index.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE traces ON CLUSTER default DROP INDEX IF EXISTS idx_user_id;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0006_add_user_id_index.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE traces ON CLUSTER default ADD INDEX IF NOT EXISTS idx_user_id user_id TYPE bloom_filter() GRANULARITY 1;
2 | ALTER TABLE traces ON CLUSTER default MATERIALIZE INDEX IF EXISTS idx_user_id;
3 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0007_add_event_log.down.sql:
--------------------------------------------------------------------------------
1 | DROP TABLE event_log ON CLUSTER default;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0007_add_event_log.up.sql:
--------------------------------------------------------------------------------
 1 | CREATE TABLE event_log ON CLUSTER default
 2 | (
 3 |     `id`          String,
 4 |     `project_id`  String,
 5 |     `entity_type` String,
 6 |     `entity_id`   String,
 7 |     `event_id`    Nullable(String),
 8 | 
 9 |     `bucket_name` String,
10 |     `bucket_path` String,
11 | 
12 |     `created_at`  DateTime64(3) DEFAULT now(),
13 |     `updated_at`  DateTime64(3) DEFAULT now()
14 | ) ENGINE = MergeTree()
15 |       ORDER BY (
16 |                 project_id,
17 |                 entity_type,
18 |                 entity_id
19 |           );
20 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0008_add_environments_column.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE traces ON CLUSTER default DROP COLUMN IF EXISTS environment;
2 | ALTER TABLE observations ON CLUSTER default DROP COLUMN IF EXISTS environment;
3 | ALTER TABLE scores ON CLUSTER default DROP COLUMN IF EXISTS environment;
4 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0008_add_environments_column.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE traces ON CLUSTER default ADD COLUMN environment LowCardinality(String) DEFAULT 'default' AFTER project_id;
2 | ALTER TABLE observations ON CLUSTER default ADD COLUMN environment LowCardinality(String) DEFAULT 'default' AFTER project_id;
3 | ALTER TABLE scores ON CLUSTER default ADD COLUMN environment LowCardinality(String) DEFAULT 'default' AFTER project_id;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0009_add_project_environments.down.sql:
--------------------------------------------------------------------------------
1 | -- Drop materialized views
2 | DROP VIEW IF EXISTS project_environments_traces_mv ON CLUSTER default;
3 | DROP VIEW IF EXISTS project_environments_observations_mv ON CLUSTER default;
4 | DROP VIEW IF EXISTS project_environments_scores_mv ON CLUSTER default;
5 | 
6 | -- Drop the project_environments table
7 | DROP TABLE IF EXISTS project_environments ON CLUSTER default;
8 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0010_add_metadata_column_on_scores.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default DROP COLUMN IF EXISTS metadata;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0010_add_metadata_column_on_scores.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default ADD COLUMN metadata Map(LowCardinality(String), String) AFTER comment;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0011_add_blob_storage_file_log.down.sql:
--------------------------------------------------------------------------------
1 | DROP TABLE blob_storage_file_log ON CLUSTER default;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0012_add_session_id_column_scores.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default DROP COLUMN IF EXISTS session_id SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0012_add_session_id_column_scores.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default ADD COLUMN session_id Nullable(String) AFTER trace_id SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0013_drop_scores_trace_id_index.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default ADD INDEX IF NOT EXISTS idx_project_trace_observation (project_id, trace_id, observation_id) TYPE bloom_filter(0.001) GRANULARITY 1 SETTINGS mutations_sync = 2;
2 | ALTER TABLE scores ON CLUSTER default MATERIALIZE INDEX IF EXISTS idx_project_trace_observation SETTINGS mutations_sync = 2;
3 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0013_drop_scores_trace_id_index.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default DROP INDEX IF EXISTS idx_project_trace_observation SETTINGS mutations_sync = 2;
2 | 
3 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0014_scores_modify_nullable_trace_id_column.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default MODIFY COLUMN trace_id Nullable(String) SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0014_scores_modify_nullable_trace_id_column.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default MODIFY COLUMN trace_id Nullable(String) SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0015_add_scores_trace_index.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default DROP INDEX IF EXISTS idx_project_trace_observation SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0015_add_scores_trace_index.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default ADD INDEX IF NOT EXISTS idx_project_trace_observation (project_id, trace_id, observation_id) TYPE bloom_filter(0.001) GRANULARITY 1 SETTINGS mutations_sync = 2;
2 | ALTER TABLE scores ON CLUSTER default MATERIALIZE INDEX IF EXISTS idx_project_trace_observation SETTINGS mutations_sync = 2;
3 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0016_add_scores_session_index.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default DROP INDEX IF EXISTS idx_project_session SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0016_add_scores_session_index.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default ADD INDEX IF NOT EXISTS idx_project_session (project_id, session_id) TYPE bloom_filter(0.001) GRANULARITY 1 SETTINGS mutations_sync = 2;
2 | ALTER TABLE scores ON CLUSTER default MATERIALIZE INDEX IF EXISTS idx_project_session SETTINGS mutations_sync = 2;
3 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0017_add_run_id_column_scores.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default DROP COLUMN IF EXISTS dataset_run_id SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0017_add_run_id_column_scores.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default ADD COLUMN dataset_run_id Nullable(String) AFTER session_id SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0018_add_scores_run_index.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default DROP INDEX IF EXISTS idx_project_dataset_run SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0018_add_scores_run_index.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ON CLUSTER default ADD INDEX IF NOT EXISTS idx_project_dataset_run (project_id, dataset_run_id) TYPE bloom_filter(0.001) GRANULARITY 1 SETTINGS mutations_sync = 2;
2 | ALTER TABLE scores ON CLUSTER default MATERIALIZE INDEX IF EXISTS idx_project_dataset_run SETTINGS mutations_sync = 2;
3 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0019_analytics_traces.down.sql:
--------------------------------------------------------------------------------
1 | DROP VIEW IF EXISTS analytics_traces ON CLUSTER default;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0019_analytics_traces.up.sql:
--------------------------------------------------------------------------------
 1 | CREATE VIEW analytics_traces ON CLUSTER default AS
 2 | SELECT
 3 |     project_id,
 4 |     toStartOfHour(timestamp) AS hour,
 5 |     uniq(id) AS countTraces,
 6 |     max(user_id IS NOT NULL) AS hasUsers,
 7 |     max(session_id IS NOT NULL) AS hasSessions,
 8 |     max(if(environment != 'default', 1, 0)) AS hasEnvironments,
 9 |     max(length(tags) > 0) AS hasTags
10 | FROM
11 |     traces
12 | WHERE toStartOfHour(timestamp) <= toStartOfHour(subtractHours(now(), 1))
13 | GROUP BY
14 |     project_id,
15 |     hour;
16 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0020_analytics_observations.down.sql:
--------------------------------------------------------------------------------
1 | DROP VIEW IF EXISTS analytics_observations ON CLUSTER default;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/clustered/0021_analytics_scores.down.sql:
--------------------------------------------------------------------------------
1 | DROP VIEW IF EXISTS analytics_scores ON CLUSTER default;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0001_traces.down.sql:
--------------------------------------------------------------------------------
1 | DROP TABLE traces;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0002_observations.down.sql:
--------------------------------------------------------------------------------
1 | DROP TABLE observations;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0003_scores.down.sql:
--------------------------------------------------------------------------------
1 | DROP TABLE scores;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0004_drop_observations_index.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE observations ADD INDEX IF NOT EXISTS idx_project_id project_id TYPE bloom_filter() GRANULARITY 1;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0004_drop_observations_index.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE observations DROP INDEX IF EXISTS idx_project_id;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0005_add_session_id_index.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE traces DROP INDEX IF EXISTS idx_session_id;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0005_add_session_id_index.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE traces ADD INDEX IF NOT EXISTS idx_session_id session_id TYPE bloom_filter() GRANULARITY 1;
2 | ALTER TABLE traces MATERIALIZE INDEX IF EXISTS idx_session_id;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0006_add_user_id_index.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE traces ON CLUSTER default DROP INDEX IF EXISTS idx_user_id;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0006_add_user_id_index.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE traces ADD INDEX IF NOT EXISTS idx_user_id user_id TYPE bloom_filter() GRANULARITY 1;
2 | ALTER TABLE traces MATERIALIZE INDEX IF EXISTS idx_user_id;
3 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0007_add_event_log.down.sql:
--------------------------------------------------------------------------------
1 | DROP TABLE event_log;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0007_add_event_log.up.sql:
--------------------------------------------------------------------------------
 1 | CREATE TABLE event_log
 2 | (
 3 |     `id`          String,
 4 |     `project_id`  String,
 5 |     `entity_type` String,
 6 |     `entity_id`   String,
 7 |     `event_id`    Nullable(String),
 8 | 
 9 |     `bucket_name` String,
10 |     `bucket_path` String,
11 | 
12 |     `created_at`  DateTime64(3) DEFAULT now(),
13 |     `updated_at`  DateTime64(3) DEFAULT now()
14 | ) ENGINE = MergeTree()
15 |       ORDER BY (
16 |                 project_id,
17 |                 entity_type,
18 |                 entity_id
19 |           );
20 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0008_add_environments_column.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE traces DROP COLUMN IF EXISTS environment;
2 | ALTER TABLE observations DROP COLUMN IF EXISTS environment;
3 | ALTER TABLE scores DROP COLUMN IF EXISTS environment;
4 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0008_add_environments_column.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE traces ADD COLUMN environment LowCardinality(String) DEFAULT 'default' AFTER project_id;
2 | ALTER TABLE observations ADD COLUMN environment LowCardinality(String) DEFAULT 'default' AFTER project_id;
3 | ALTER TABLE scores ADD COLUMN environment LowCardinality(String) DEFAULT 'default' AFTER project_id;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0009_add_project_environments.down.sql:
--------------------------------------------------------------------------------
1 | -- Drop materialized views
2 | DROP VIEW IF EXISTS project_environments_traces_mv;
3 | DROP VIEW IF EXISTS project_environments_observations_mv;
4 | DROP VIEW IF EXISTS project_environments_scores_mv;
5 | 
6 | -- Drop the project_environments table
7 | DROP TABLE IF EXISTS project_environments;
8 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0010_add_metadata_column_on_scores.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores DROP COLUMN IF EXISTS metadata;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0010_add_metadata_column_on_scores.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ADD COLUMN metadata Map(LowCardinality(String), String) AFTER comment;


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0011_add_blob_storage_file_log.down.sql:
--------------------------------------------------------------------------------
1 | DROP TABLE blob_storage_file_log;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0012_add_session_id_column_scores.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores DROP COLUMN IF EXISTS session_id SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0012_add_session_id_column_scores.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ADD COLUMN session_id Nullable(String) AFTER trace_id SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0013_drop_scores_trace_id_index.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ADD INDEX IF NOT EXISTS idx_project_trace_observation (project_id, trace_id, observation_id) TYPE bloom_filter(0.001) GRANULARITY 1 SETTINGS mutations_sync = 2;
2 | ALTER TABLE scores MATERIALIZE INDEX IF EXISTS idx_project_trace_observation SETTINGS mutations_sync = 2;
3 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0013_drop_scores_trace_id_index.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores DROP INDEX IF EXISTS idx_project_trace_observation SETTINGS mutations_sync = 2;
2 | 
3 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0014_scores_modify_nullable_trace_id_column.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores MODIFY COLUMN trace_id Nullable(String) SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0014_scores_modify_nullable_trace_id_column.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores MODIFY COLUMN trace_id Nullable(String) SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0015_add_scores_trace_index.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores DROP INDEX IF EXISTS idx_project_trace_observation SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0015_add_scores_trace_index.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ADD INDEX IF NOT EXISTS idx_project_trace_observation (project_id, trace_id, observation_id) TYPE bloom_filter(0.001) GRANULARITY 1 SETTINGS mutations_sync = 2; 
2 | ALTER TABLE scores MATERIALIZE INDEX IF EXISTS idx_project_trace_observation SETTINGS mutations_sync = 2;
3 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0016_add_scores_session_index.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores DROP INDEX IF EXISTS idx_project_session SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0016_add_scores_session_index.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ADD INDEX IF NOT EXISTS idx_project_session (project_id, session_id) TYPE bloom_filter(0.001) GRANULARITY 1 SETTINGS mutations_sync = 2;
2 | ALTER TABLE scores MATERIALIZE INDEX IF EXISTS idx_project_session SETTINGS mutations_sync = 2;
3 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0017_add_run_id_column_scores.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores DROP COLUMN IF EXISTS dataset_run_id SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0017_add_run_id_column_scores.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ADD COLUMN dataset_run_id Nullable(String) AFTER session_id SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0018_add_scores_run_index.down.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores DROP INDEX IF EXISTS idx_project_dataset_run SETTINGS mutations_sync = 2;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0018_add_scores_run_index.up.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE scores ADD INDEX IF NOT EXISTS idx_project_dataset_run (project_id, dataset_run_id) TYPE bloom_filter(0.001) GRANULARITY 1 SETTINGS mutations_sync = 2;
2 | ALTER TABLE scores MATERIALIZE INDEX IF EXISTS idx_project_dataset_run SETTINGS mutations_sync = 2;
3 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0019_analytics_traces.down.sql:
--------------------------------------------------------------------------------
1 | DROP VIEW IF EXISTS analytics_traces;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0019_analytics_traces.up.sql:
--------------------------------------------------------------------------------
 1 | CREATE VIEW analytics_traces AS
 2 | SELECT
 3 |     project_id,
 4 |     toStartOfHour(timestamp) AS hour,
 5 |     uniq(id) AS countTraces,
 6 |     max(user_id IS NOT NULL) AS hasUsers,
 7 |     max(session_id IS NOT NULL) AS hasSessions,
 8 |     max(if(environment != 'default', 1, 0)) AS hasEnvironments,
 9 |     max(length(tags) > 0) AS hasTags
10 | FROM
11 |     traces
12 | WHERE toStartOfHour(timestamp) <= toStartOfHour(subtractHours(now(), 1))
13 | GROUP BY
14 |     project_id,
15 |     hour;
16 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0020_analytics_observations.down.sql:
--------------------------------------------------------------------------------
1 | DROP VIEW IF EXISTS analytics_observations;
2 | 


--------------------------------------------------------------------------------
/packages/shared/clickhouse/migrations/unclustered/0021_analytics_scores.down.sql:
--------------------------------------------------------------------------------
1 | DROP VIEW IF EXISTS analytics_scores;
2 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230522094431_endtime_optional/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "observations" ALTER COLUMN "end_time" DROP NOT NULL;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230522131516_default_timestamp/migration.sql:
--------------------------------------------------------------------------------
 1 | /*
 2 |   Warnings:
 3 | 
 4 |   - You are about to drop the column `createdAt` on the `metrics` table. All the data in the column will be lost.
 5 | 
 6 | */
 7 | -- AlterTable
 8 | ALTER TABLE "metrics" DROP COLUMN "createdAt",
 9 | ADD COLUMN     "timestamp" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP;
10 | 
11 | -- AlterTable
12 | ALTER TABLE "observations" ALTER COLUMN "start_time" SET DEFAULT CURRENT_TIMESTAMP;
13 | 
14 | -- AlterTable
15 | ALTER TABLE "traces" ALTER COLUMN "timestamp" SET DEFAULT CURRENT_TIMESTAMP;
16 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230529140133_user_add_pw/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "User" ADD COLUMN     "password" TEXT;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230618125818_remove_status_from_trace/migration.sql:
--------------------------------------------------------------------------------
 1 | /*
 2 |   Warnings:
 3 | 
 4 |   - You are about to drop the column `status` on the `traces` table. All the data in the column will be lost.
 5 |   - You are about to drop the column `status_message` on the `traces` table. All the data in the column will be lost.
 6 | 
 7 | */
 8 | -- AlterTable
 9 | ALTER TABLE "traces" DROP COLUMN "status",
10 | DROP COLUMN "status_message";
11 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230622114254_new_oservations/migration.sql:
--------------------------------------------------------------------------------
 1 | BEGIN;
 2 | 
 3 | ALTER TABLE "observations"
 4 | RENAME COLUMN "prompt" TO "input";
 5 | 
 6 | ALTER TABLE "observations"
 7 | ADD COLUMN "output_temp" JSONB;
 8 | 
 9 | UPDATE "observations"
10 | SET "output_temp" = json_build_object('completion', "observations"."completion");
11 | 
12 | ALTER TABLE "observations"
13 | DROP COLUMN "completion";
14 | 
15 | ALTER TABLE "observations"
16 | RENAME COLUMN "output_temp" TO "output";
17 | 
18 | COMMIT;


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230623172401_observation_add_level_and_status_message/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateEnum
2 | CREATE TYPE "ObservationLevel" AS ENUM ('DEBUG', 'DEFAULT', 'WARNING', 'ERROR');
3 | 
4 | -- AlterTable
5 | ALTER TABLE "observations" ADD COLUMN     "level" "ObservationLevel" NOT NULL DEFAULT 'DEFAULT',
6 | ADD COLUMN     "status_message" TEXT;
7 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230626095337_external_trace_id/migration.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE "traces" ADD COLUMN     "external_id" TEXT;
2 | CREATE UNIQUE INDEX "traces_project_id_external_id_key" ON "traces"("project_id", "external_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230705160335_add_created_updated_timestamps/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "memberships" ADD COLUMN     "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
3 | ADD COLUMN     "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP;
4 | 
5 | -- AlterTable
6 | ALTER TABLE "users" ADD COLUMN     "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
7 | ADD COLUMN     "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP;
8 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230706195819_add_completion_start_time/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "observations" ADD COLUMN     "completion_start_time" TIMESTAMP(3);
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230707132314_traces_project_id_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX "traces_project_id_idx" ON "traces"("project_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230707133415_user_add_email_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX "Account_user_id_idx" ON "Account"("user_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230710105741_added_indices/migration.sql:
--------------------------------------------------------------------------------
 1 | -- DropIndex
 2 | DROP INDEX "traces_project_id_idx";
 3 | 
 4 | -- CreateIndex
 5 | CREATE INDEX "observations_trace_id_type_idx" ON "observations"("trace_id", "type");
 6 | 
 7 | -- CreateIndex
 8 | CREATE INDEX "scores_value_idx" ON "scores"("value");
 9 | 
10 | -- CreateIndex
11 | CREATE INDEX "traces_project_id_name_idx" ON "traces"("project_id", "name");
12 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230710114928_traces_add_user_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | DROP INDEX "traces_project_id_name_idx";
3 | 
4 | -- AlterTable
5 | ALTER TABLE "traces" ADD COLUMN     "user_id" TEXT;
6 | 
7 | -- CreateIndex
8 | CREATE INDEX "traces_project_id_name_user_id_idx" ON "traces"("project_id", "name", "user_id");
9 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230710200816_scores_add_comment/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "scores" ADD COLUMN     "comment" TEXT;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230711104810_traces_add_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | DROP INDEX "traces_project_id_name_user_id_idx";
3 | 
4 | -- CreateIndex
5 | CREATE INDEX "traces_project_id_name_user_id_external_id_idx" ON "traces"("project_id", "name", "user_id", "external_id");
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230711110517_memberships_add_userid_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX "memberships_user_id_idx" ON "memberships"("user_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230717190411_users_feature_flags/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "users" ADD COLUMN     "feature_flags" TEXT[] DEFAULT ARRAY[]::TEXT[];
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230720162550_tokens/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "observations" ADD COLUMN     "completion_tokens" INTEGER,
3 | ADD COLUMN     "prompt_tokens" INTEGER,
4 | ADD COLUMN     "total_tokens" INTEGER;
5 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230720164603_migrate_tokens/migration.sql:
--------------------------------------------------------------------------------
1 | -- This is an empty migration.
2 | UPDATE observations
3 |   SET prompt_tokens = CAST(usage::json->>'promptTokens' AS INTEGER),
4 |   completion_tokens = CAST(usage::json->>'completionTokens' AS INTEGER),
5 |   total_tokens = CAST(usage::json->>'totalTokens' AS INTEGER);


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230721111651_drop_usage_json/migration.sql:
--------------------------------------------------------------------------------
1 | /*
2 |   Warnings:
3 | 
4 |   - You are about to drop the column `usage` on the `observations` table. All the data in the column will be lost.
5 | 
6 | */
7 | -- AlterTable
8 | ALTER TABLE "observations" DROP COLUMN "usage";
9 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230731162154_score_value_float/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "scores" ALTER COLUMN "value" SET DATA TYPE DOUBLE PRECISION;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230803093326_add_release_and_version/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "observations" ADD COLUMN     "version" TEXT;
3 | 
4 | -- AlterTable
5 | ALTER TABLE "traces" ADD COLUMN     "release" TEXT,
6 | ADD COLUMN     "version" TEXT;
7 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230809093636_remove_foreign_keys/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropForeignKey
2 | ALTER TABLE "observations" DROP CONSTRAINT "observations_parent_observation_id_fkey";
3 | 
4 | -- DropForeignKey
5 | ALTER TABLE "observations" DROP CONSTRAINT "observations_trace_id_fkey";
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230810191452_traceid_nullable_on_observations/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "observations" ALTER COLUMN "trace_id" DROP NOT NULL;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230810191453_project_id_not_null/migration.sql:
--------------------------------------------------------------------------------
1 | -- Applied in separate migration after application release to minimize ingestion downtime
2 | ALTER TABLE "observations"
3 | ALTER COLUMN "project_id" SET NOT NULL;
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230814184705_add_viewer_membership_role/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterEnum
2 | ALTER TYPE "MembershipRole" ADD VALUE 'VIEWER';
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230901155252_add_pricings_table/migration.sql:
--------------------------------------------------------------------------------
 1 | -- CreateEnum
 2 | CREATE TYPE "PricingUnit" AS ENUM ('PER_1000_TOKENS');
 3 | 
 4 | -- CreateEnum
 5 | CREATE TYPE "TokenType" AS ENUM ('PROMPT', 'COMPLETION', 'TOTAL');
 6 | 
 7 | -- CreateTable
 8 | CREATE TABLE "pricings" (
 9 |     "id" TEXT NOT NULL,
10 |     "model_name" TEXT NOT NULL,
11 |     "pricing_unit" "PricingUnit" NOT NULL DEFAULT 'PER_1000_TOKENS',
12 |     "price" DECIMAL(65,30) NOT NULL,
13 |     "currency" TEXT NOT NULL DEFAULT 'USD',
14 |     "token_type" "TokenType" NOT NULL,
15 | 
16 |     CONSTRAINT "pricings_pkey" PRIMARY KEY ("id")
17 | );
18 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230907204921_add_cron_jobs_table/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateTable
2 | CREATE TABLE "cron_jobs" (
3 |     "name" TEXT NOT NULL,
4 |     "last_run" TIMESTAMP(3),
5 | 
6 |     CONSTRAINT "cron_jobs_pkey" PRIMARY KEY ("name")
7 | );
8 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230907225603_projects_updated_at/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "projects" ADD COLUMN     "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230907225604_api_keys_publishable_to_public/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | DROP INDEX "api_keys_publishable_key_key";
3 | 
4 | -- RENAME column from "publishable_key" to "public_key" on table "api_keys"
5 | ALTER TABLE "api_keys" rename column "publishable_key" to "public_key";
6 | 
7 | -- CreateIndex
8 | CREATE UNIQUE INDEX "api_keys_public_key_key" ON "api_keys"("public_key");
9 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230910164603_cron_add_state/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "cron_jobs" ADD COLUMN     "state" TEXT;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230912115644_add_trace_public_bool/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "traces" ADD COLUMN     "public" BOOLEAN NOT NULL DEFAULT false;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230918180320_add_indices/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX "observations_start_time_idx" ON "observations"("start_time");
3 | 
4 | -- CreateIndex
5 | CREATE INDEX "traces_timestamp_idx" ON "traces"("timestamp");
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20230922030325_add_observation_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX "observations_project_id_idx" ON "observations"("project_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231004005909_add_parent_observation_id_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX "observations_parent_observation_id_idx" ON "observations"("parent_observation_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231005064433_add_release_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX "traces_release_idx" ON "traces"("release");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231012161041_add_events_table/migration.sql:
--------------------------------------------------------------------------------
 1 | -- CreateTable
 2 | CREATE TABLE "events" (
 3 |     "id" TEXT NOT NULL,
 4 |     "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
 5 |     "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
 6 |     "project_id" TEXT NOT NULL,
 7 |     "data" JSONB NOT NULL,
 8 |     "url" TEXT,
 9 |     "method" TEXT,
10 | 
11 |     CONSTRAINT "events_pkey" PRIMARY KEY ("id")
12 | );
13 | 
14 | -- AddForeignKey
15 | ALTER TABLE "events" ADD CONSTRAINT "events_project_id_fkey" FOREIGN KEY ("project_id") REFERENCES "projects"("id") ON DELETE CASCADE ON UPDATE CASCADE;
16 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231014131841_users_add_admin_flag/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "users" ADD COLUMN     "admin" BOOLEAN NOT NULL DEFAULT false;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231018130032_add_per_1000_chars_pricing/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterEnum
2 | ALTER TYPE "PricingUnit" ADD VALUE 'PER_1000_CHARS';
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231021182825_user_emails_all_lowercase/migration.sql:
--------------------------------------------------------------------------------
1 | -- Due to the unique constraint on the email column, we need to make sure that all emails are in lowercase.
2 | -- This migration will update all existing emails to be lowercase.
3 | -- This migration fails if there are duplicate emails in the database.
4 | 
5 | UPDATE "users" SET "email" = LOWER("email");
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231025153548_add_headers_to_events/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "events" ADD COLUMN     "headers" JSONB NOT NULL DEFAULT '{}';
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231030184329_events_add_index_on_projectid/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX "events_project_id_idx" ON "events"("project_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231104004529_scores_add_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX "scores_trace_id_idx" ON "scores" USING HASH ("trace_id");
3 | 
4 | -- CreateIndex
5 | CREATE INDEX "scores_observation_id_idx" ON "scores" USING HASH ("observation_id");
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231106213824_add_openai_models/migration.sql:
--------------------------------------------------------------------------------
 1 | -- This is an empty migration.
 2 | 
 3 | INSERT INTO pricings (
 4 |   id,
 5 |   model_name, 
 6 |   pricing_unit, 
 7 |   price,
 8 |   currency,
 9 |   token_type
10 | )
11 | VALUES
12 |   ('clm0obv1u00003b6lc2etkzfu','gpt-4-1106-preview', 'PER_1000_TOKENS', 0.01, 'USD', 'PROMPT'),
13 |   ('clm0obv1u00003b6lc2etkzfg','gpt-4-1106-preview', 'PER_1000_TOKENS', 0.03, 'USD', 'COMPLETION'),
14 |   ('clm0obv1u00013b6l4gdl83vs','gpt-4-1106-vision-preview	', 'PER_1000_TOKENS', 0.01, 'USD', 'PROMPT'),
15 |   ('clm0obv1u00013b6l4gjl83vs','gpt-4-1106-vision-preview	', 'PER_1000_TOKENS', 0.03, 'USD', 'COMPLETION')


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231110012457_observation_created_at/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "observations" ADD COLUMN "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231110012829_observation_created_at_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX "observations_created_at_idx" ON "observations"("created_at");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231112095703_observations_add_unique_constraint/migration.sql:
--------------------------------------------------------------------------------
1 | /*
2 |   Warnings:
3 | 
4 |   - A unique constraint covering the columns `[id,project_id]` on the table `observations` will be added. If there are existing duplicate values, this will fail.
5 | 
6 | */
7 | -- CreateIndex
8 | CREATE UNIQUE INDEX "observations_id_project_id_key" ON "observations"("id", "project_id");
9 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231116005353_scores_unique_id_projectid/migration.sql:
--------------------------------------------------------------------------------
1 | /*
2 |   Warnings:
3 | 
4 |   - A unique constraint covering the columns `[id,trace_id]` on the table `scores` will be added. If there are existing duplicate values, this will fail.
5 | 
6 | */
7 | -- CreateIndex
8 | CREATE UNIQUE INDEX "scores_id_trace_id_key" ON "scores"("id", "trace_id");
9 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231119171939_cron_add_job_started_at/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "cron_jobs" ADD COLUMN     "job_started_at" TIMESTAMP(3);
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231119171940_bookmarked/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- AlterTable
3 | ALTER TABLE "traces" ADD COLUMN "bookmarked" BOOLEAN NOT NULL DEFAULT false;
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231204223505_add_unit_to_observations/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | -- Adding this migration does not lock the postgres table. For non volaitile data, the default value is stored in the 
3 | -- table metadata and accessed on read query time. No table re-write is required (https://www.postgresql.org/docs/current/sql-altertable.html#:~:text=When%20a%20column%20is%20added,is%20specified%2C%20NULL%20is%20used.)
4 | ALTER TABLE "observations" ADD COLUMN "unit" TEXT NOT NULL DEFAULT 'TOKENS';


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231223230007_cloud_config/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "projects" ADD COLUMN     "cloud_config" JSONB;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20231223230008_accounts_add_cols_azure_ad_auth/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "Account" ADD COLUMN     "expires_in" INTEGER,
3 | ADD COLUMN     "ext_expires_in" INTEGER;
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240104210051_add_model_indices/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "observations_model_idx" ON "observations"("model");
3 | 
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240104210052_add_model_indices_pricing/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "pricings_model_name_idx" ON "pricings"("model_name");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240105010215_add_tags_in_traces/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "traces" ADD COLUMN     "tags" TEXT[] DEFAULT ARRAY[]::TEXT[];
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240105170551_index_tags_in_traces/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX "traces_tags_idx" ON "traces" USING GIN ("tags" array_ops);
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240106195340_drop_dataset_status/migration.sql:
--------------------------------------------------------------------------------
1 | /*
2 |   Warnings:
3 | 
4 |   - You are about to drop the column `status` on the `datasets` table. All the data in the column will be lost.
5 | 
6 | */
7 | -- AlterTable
8 | ALTER TABLE "datasets" DROP COLUMN "status";
9 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240111152124_add_gpt_35_pricing/migration.sql:
--------------------------------------------------------------------------------
 1 | -- Migration to add gpt-35 spelling
 2 | 
 3 | INSERT INTO pricings (
 4 |   id,
 5 |   model_name, 
 6 |   pricing_unit, 
 7 |   price,
 8 |   currency,
 9 |   token_type
10 | )
11 | VALUES
12 |   ('clqqpc2pr000008l3hvy63gxy1','gpt-35-turbo-1106', 'PER_1000_TOKENS', 0.001, 'USD', 'PROMPT'),
13 |   ('clqqpcb6d000208l3atrfbmou1','gpt-35-turbo-1106', 'PER_1000_TOKENS', 0.002, 'USD', 'COMPLETION'),
14 |   ('clqqpdh45000008lfgrnx76cv1','gpt-35-turbo-instruct', 'PER_1000_TOKENS', 0.0015, 'USD', 'PROMPT'),
15 |   ('clqqpdjya000108lf3s4b4c4m1','gpt-35-turbo-instruct', 'PER_1000_TOKENS', 0.002, 'USD', 'COMPLETION')
16 | ON CONFLICT (id) DO NOTHING;


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240117151938_traces_remove_unique_id_external/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | DROP INDEX "traces_project_id_external_id_key";
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240117165747_add_cost_to_observations/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "observations" ADD COLUMN     "input_cost" DECIMAL(65,30),
3 | ADD COLUMN     "output_cost" DECIMAL(65,30),
4 | ADD COLUMN     "total_cost" DECIMAL(65,30);
5 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240118204936_add_internal_model/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "observations" ADD COLUMN     "internal_model" TEXT;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240118235424_add_index_to_models/migration.sql:
--------------------------------------------------------------------------------
 1 | /*
 2 |   Warnings:
 3 | 
 4 |   - A unique constraint covering the columns `[project_id,model_name,start_date,unit]` on the table `models` will be added. If there are existing duplicate values, this will fail.
 5 | 
 6 | */
 7 | -- CreateIndex
 8 | CREATE INDEX "models_project_id_model_name_idx" ON "models"("project_id", "model_name");
 9 | 
10 | -- CreateIndex
11 | CREATE UNIQUE INDEX "models_project_id_model_name_start_date_unit_key" ON "models"("project_id", "model_name", "start_date", "unit");
12 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240119140941_add_tokenizer_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "models" ADD COLUMN     "tokenizer_id" TEXT;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240119164147_make_model_params_nullable/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "models" ALTER COLUMN "tokenizer_config" DROP NOT NULL;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240130100110_usage_unit_nullable/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "models" ALTER COLUMN "unit" DROP DEFAULT;
3 | 
4 | -- AlterTable
5 | ALTER TABLE "observations" ALTER COLUMN "unit" DROP NOT NULL,
6 | ALTER COLUMN "unit" DROP DEFAULT;
7 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240214232619_prompts_add_indicies/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX "prompts_project_id_id_idx" ON "prompts"("project_id", "id");
3 | 
4 | -- CreateIndex
5 | CREATE INDEX "prompts_project_id_idx" ON "prompts"("project_id");
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240215224148_update_openai_pricing/migration.sql:
--------------------------------------------------------------------------------
 1 | -- This is an empty migration.
 2 | 
 3 | INSERT INTO models (
 4 |   id,
 5 |   project_id,
 6 |   model_name,
 7 |   match_pattern,
 8 |   start_date,
 9 |   input_price,
10 |   output_price,
11 |   total_price,
12 |   unit,
13 |   tokenizer_id,
14 |   tokenizer_config
15 | )
16 | VALUES
17 |   ('clsnq07bn000008l4e46v1ll8', NULL, 'gpt-4-turbo-preview', '(?i)^(gpt-4-turbo-preview)
#39;, '2023-11-06', 0.00001, 0.00003, NULL, 'TOKENS', 'openai', '{ "tokensPerMessage": 3, "tokensPerName": 1, "tokenizerModel": "gpt-4" }')


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240219162415_add_prompt_config/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "prompts" ADD COLUMN     "config" JSONB NOT NULL DEFAULT '{}';
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240226165118_add_observations_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "observations_project_id_start_time_type_idx" ON "observations"("project_id", "start_time", "type");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240226182815_add_model_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "models_project_id_model_name_start_date_unit_idx" ON "models"("project_id", "model_name", "start_date", "unit");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240226183642_add_observations_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "observations_project_id_internal_model_start_time_unit_idx" ON "observations"("project_id", "internal_model", "start_time", "unit");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240226202040_add_observations_trace_id_project_id_start_time_idx/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "observations_trace_id_project_id_start_time_idx" ON "observations"("trace_id", "project_id", "start_time");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240226202041_add_observations_trace_id_project_id_type_start_time_idx/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "observations_trace_id_project_id_type_start_time_idx" ON "observations"("trace_id", "project_id", "type", "start_time");


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240227112101_index_prompt_id_in_observations/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY IF NOT EXISTS "observations_prompt_id_idx" ON "observations"("prompt_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240304123642_traces_view/migration.sql:
--------------------------------------------------------------------------------
1 | CREATE VIEW trace_metrics_view AS
2 | SELECT
3 |     t.id,
4 |     EXTRACT(EPOCH FROM COALESCE(MAX(o.end_time), MAX(o.start_time))) - EXTRACT(EPOCH FROM MIN(o.start_time))::double precision AS duration
5 | FROM
6 |     traces t
7 |     LEFT JOIN observations o ON t.id = o.trace_id
8 | group by t.project_id, t.id


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240304123642_traces_view_improvement/migration.sql:
--------------------------------------------------------------------------------
 1 | DROP VIEW trace_metrics_view;
 2 | 
 3 | 
 4 | CREATE OR REPLACE VIEW traces_view AS
 5 | WITH observations_metrics AS (
 6 |     SELECT
 7 |         trace_id,
 8 |         project_id,
 9 |         EXTRACT(EPOCH FROM COALESCE(MAX(o.end_time), MAX(o.start_time))) - EXTRACT(EPOCH FROM MIN(o.start_time))::double precision AS duration
10 |     FROM
11 |         observations o
12 |     GROUP BY
13 |         project_id, trace_id
14 | )
15 | SELECT
16 |     t.*,
17 |     o.duration
18 | FROM
19 |     traces t
20 |     LEFT JOIN observations_metrics o ON t.id = o.trace_id and t.project_id = o.project_id


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240304222519_scores_add_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "scores_timestamp_idx" ON "scores"("timestamp");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240305095119_add_observations_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "observations_trace_id_project_id_idx" ON "observations"("trace_id", "project_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240305100713_traces_add_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "traces_id_user_id_idx" ON "traces"("id", "user_id");


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240307185543_score_add_source_nullable/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateEnum
2 | CREATE TYPE "ScoreSource" AS ENUM ('API', 'REVIEW');
3 | 
4 | -- AlterTable
5 | ALTER TABLE "scores" ADD COLUMN     "source" "ScoreSource" NOT NULL DEFAULT 'API';
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240307185544_score_add_name_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "scores_source_idx" ON "scores"("source");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240307185725_backfill_score_source/migration.sql:
--------------------------------------------------------------------------------
1 | -- scores previously created in the Langfuse UI all had the name 'manual-score'
2 | UPDATE "scores"
3 | SET "source" = 'REVIEW'::"ScoreSource"
4 | WHERE "name" = 'manual-score';
5 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240312195727_score_source_drop_default/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "scores" ALTER COLUMN "source" DROP DEFAULT;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240314090110_claude_model/migration.sql:
--------------------------------------------------------------------------------
 1 | INSERT INTO models (
 2 |   id,
 3 |   project_id,
 4 |   model_name,
 5 |   match_pattern,
 6 |   start_date,
 7 |   input_price,
 8 |   output_price,
 9 |   total_price,
10 |   unit,
11 |   tokenizer_id,
12 |   tokenizer_config
13 | )
14 | VALUES
15 |   -- https://docs.anthropic.com/claude/docs/models-overview, https://docs.anthropic.com/claude/docs/quickstart-guide
16 |   ('cltr0w45b000008k1407o9qv1', NULL, 'claude-3-haiku-20240307', '(?i)^(claude-3-haiku-20240307)
#39;, NULL, 0.00000025, 0.00000125, NULL, 'TOKENS', 'claude', NULL)
17 | 
18 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240325211959_remove_example_table/migration.sql:
--------------------------------------------------------------------------------
1 | /*
2 |   Warnings:
3 | 
4 |   - You are about to drop the `Example` table. If the table is not empty, all the data it contains will be lost.
5 | 
6 | */
7 | -- DropTable
8 | DROP TABLE "Example";
9 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240325212245_dataset_runs_add_metadata/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "dataset_runs" ADD COLUMN     "metadata" JSONB;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240326114211_dataset_run_item_bind_to_trace/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "dataset_run_items" ADD COLUMN     "trace_id" TEXT,
3 | ALTER COLUMN "observation_id" DROP NOT NULL;
4 | 
5 | -- AddForeignKey
6 | ALTER TABLE "dataset_run_items" ADD CONSTRAINT "dataset_run_items_trace_id_fkey" FOREIGN KEY ("trace_id") REFERENCES "traces"("id") ON DELETE CASCADE ON UPDATE CASCADE;
7 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240326114337_dataset_run_item_backfill_trace_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- Backfill trace_id for existing run_items based on the linked observation
2 | UPDATE dataset_run_items
3 | SET trace_id = observations.trace_id
4 | FROM observations 
5 | WHERE dataset_run_items.observation_id = observations.id;


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240326115136_dataset_run_item_traceid_non_null/migration.sql:
--------------------------------------------------------------------------------
1 | /*
2 |   Warnings:
3 | 
4 |   - Made the column `trace_id` on table `dataset_run_items` required. This step will fail if there are existing NULL values in that column.
5 | 
6 | */
7 | -- AlterTable
8 | ALTER TABLE "dataset_run_items" ALTER COLUMN "trace_id" SET NOT NULL;
9 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240326115424_dataset_run_item_index_trace/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "dataset_run_items_trace_id_idx" ON "dataset_run_items"("trace_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240328065738_dataset_item_input_nullable/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "dataset_items" ALTER COLUMN "input" DROP NOT NULL;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240404203640_dataset_item_source_trace_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "dataset_items" ADD COLUMN     "source_trace_id" TEXT;
3 | 
4 | -- AddForeignKey
5 | ALTER TABLE "dataset_items" ADD CONSTRAINT "dataset_items_source_trace_id_fkey" FOREIGN KEY ("source_trace_id") REFERENCES "traces"("id") ON DELETE SET NULL ON UPDATE CASCADE;
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240404210315_dataset_add_descriptions/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "dataset_runs" ADD COLUMN     "description" TEXT;
3 | 
4 | -- AlterTable
5 | ALTER TABLE "datasets" ADD COLUMN     "description" TEXT;
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240404232317_dataset_items_backfill_source_trace_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- Backfill source_trace_id for existing dataset_items based on the linked source_observation_id
2 | UPDATE dataset_items
3 | SET source_trace_id = observations.trace_id
4 | FROM observations
5 | WHERE dataset_items.source_observation_id = observations.id
6 |   AND dataset_items.source_observation_id IS NOT NULL
7 |   AND dataset_items.source_trace_id IS NULL


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240405124810_prompt_to_json/migration.sql:
--------------------------------------------------------------------------------
 1 | BEGIN;
 2 | 
 3 | ALTER TABLE prompts
 4 | ADD COLUMN json_prompt JSONB;
 5 | 
 6 | UPDATE prompts
 7 | SET json_prompt = to_json(prompt::text)::json;
 8 | 
 9 | ALTER TABLE prompts
10 | DROP COLUMN prompt;
11 | 
12 | ALTER TABLE prompts
13 | RENAME COLUMN json_prompt TO prompt;
14 | 
15 | ALTER TABLE prompts
16 | ALTER COLUMN prompt SET NOT NULL;
17 | 
18 | ALTER TABLE prompts
19 | ADD COLUMN type TEXT NOT NULL DEFAULT 'text';
20 | 
21 | COMMIT;
22 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240408134328_prompt_table_add_tags/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "prompts" ADD COLUMN     "tags" TEXT[] DEFAULT ARRAY[]::TEXT[];
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240408134330_prompt_table_add_index_to_tags/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "prompts_tags_idx" ON "prompts" USING GIN ("tags" array_ops);
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240411194142_update_job_config_status/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateEnum
2 | CREATE TYPE "JobConfigState" AS ENUM ('ACTIVE', 'INACTIVE');
3 | 
4 | -- AlterTable
5 | ALTER TABLE "job_configurations" ADD COLUMN     "status" "JobConfigState" NOT NULL DEFAULT 'ACTIVE';
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240411224142_update_models/migration.sql:
--------------------------------------------------------------------------------
 1 | INSERT INTO models (
 2 |   id,
 3 |   project_id,
 4 |   model_name,
 5 |   match_pattern,
 6 |   start_date,
 7 |   input_price,
 8 |   output_price,
 9 |   total_price,
10 |   unit,
11 |   tokenizer_id,
12 |   tokenizer_config
13 | )
14 | VALUES
15 |   -- https://platform.openai.com/docs/models/continuous-model-upgrades
16 |   ('cluvpl4ls000008l6h2gx3i07', NULL, 'gpt-4-turbo', '(?i)^(gpt-4-turbo)
#39;, NULL, 0.00001, 0.00003, NULL, 'TOKENS', 'openai', '{ "tokensPerMessage": 3, "tokensPerName": 1, "tokenizerModel": "gpt-4-1106-preview" }')


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240414203636_ee_add_sso_configs/migration.sql:
--------------------------------------------------------------------------------
 1 | -- CreateTable
 2 | CREATE TABLE "sso_configs" (
 3 |     "domain" TEXT NOT NULL,
 4 |     "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
 5 |     "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
 6 |     "auth_provider" TEXT NOT NULL,
 7 |     "auth_config" JSONB,
 8 | 
 9 |     CONSTRAINT "sso_configs_pkey" PRIMARY KEY ("domain")
10 | );
11 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240415235737_index_models_model_name/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "models_model_name_idx" ON "models"("model_name");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240416173813_add_internal_model_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "observations_internal_model_idx" ON "observations"("internal_model");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240417102742_metadata_on_dataset_and_dataset_item/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "dataset_items" ADD COLUMN     "metadata" JSONB;
3 | 
4 | -- AlterTable
5 | ALTER TABLE "datasets" ADD COLUMN     "metadata" JSONB;
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240420134232_posthog_integration_created_at/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "posthog_integrations" ADD COLUMN     "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240424150909_add_job_execution_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX "job_executions_project_id_status_idx" ON "job_executions"("project_id", "status");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240429124411_add_prompt_version_labels/migration.sql:
--------------------------------------------------------------------------------
 1 | BEGIN;
 2 | 
 3 | -- Step 1: Alter the 'prompts' table to add the 'labels' column
 4 | ALTER TABLE prompts
 5 | ADD COLUMN labels TEXT[] DEFAULT ARRAY[]::TEXT[];
 6 | 
 7 | -- Step 2: Update the 'labels' column to include 'production' for active prompts
 8 | UPDATE prompts
 9 | SET labels = array_append(labels, 'production')
10 | WHERE is_active = TRUE;
11 | 
12 | -- Step 3: Drop the required constraint on 'is_active' column.
13 | ALTER TABLE prompts
14 | ALTER COLUMN is_active DROP NOT NULL;
15 | 
16 | COMMIT;


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240429194411_add_latest_prompt_tag/migration.sql:
--------------------------------------------------------------------------------
 1 | UPDATE
 2 | 	prompts
 3 | SET
 4 | 	labels = array_append(labels, 'latest')
 5 | WHERE
 6 | 	id = (
 7 | 		SELECT
 8 | 			id
 9 | 		FROM
10 | 			prompts AS p2
11 | 		WHERE
12 | 			p2.name = prompts.name
13 | 		ORDER BY
14 | 			created_at DESC
15 | 		LIMIT 1);


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240503125742_traces_add_createdat_updatedat/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "traces" ADD COLUMN     "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
3 | ADD COLUMN     "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP;
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240503130335_traces_index_created_at/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | 
3 | CREATE INDEX CONCURRENTLY "traces_created_at_idx" ON "traces"("created_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240503130520_traces_index_updated_at/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | 
3 | CREATE INDEX CONCURRENTLY "traces_updated_at_idx" ON "traces"("updated_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240508132621_scores_add_project_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "scores" ADD COLUMN     "project_id" TEXT;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240508132735_scores_add_projectid_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "scores_project_id_idx" ON "scores"("project_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240508132736_scores_backfill_project_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- Backfill project_id on existing scores based on linked trace_id
2 | UPDATE scores
3 | SET project_id = traces.project_id
4 | FROM traces 
5 | WHERE scores.trace_id = traces.id AND scores.project_id IS NULL;
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240512155021_scores_drop_fk_on_traces_and_observations/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropForeignKey
2 | ALTER TABLE "scores" DROP CONSTRAINT "scores_observation_id_fkey";
3 | 
4 | -- DropForeignKey
5 | ALTER TABLE "scores" DROP CONSTRAINT "scores_trace_id_fkey";
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240512155022_scores_non_null_and_add_fk_project_id/migration.sql:
--------------------------------------------------------------------------------
 1 | /*
 2 |   Warnings:
 3 | 
 4 |   - Made the column `project_id` on table `scores` required. This step will fail if there are existing NULL values in that column.
 5 | 
 6 | */
 7 | -- AlterTable
 8 | ALTER TABLE "scores" ALTER COLUMN "project_id" SET NOT NULL;
 9 | 
10 | -- AddForeignKey
11 | ALTER TABLE "scores" ADD CONSTRAINT "scores_project_id_fkey" FOREIGN KEY ("project_id") REFERENCES "projects"("id") ON DELETE CASCADE ON UPDATE CASCADE;
12 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240513082203_scores_unique_id_and_projectid_instead_of_id_and_traceid/migration.sql:
--------------------------------------------------------------------------------
1 | /*
2 |   Warnings:
3 | 
4 |   - A unique constraint covering the columns `[id,project_id]` on the table `scores` will be added. If there are existing duplicate values, this will fail.
5 | 
6 | */
7 | -- DropIndex
8 | DROP INDEX "scores_id_trace_id_key";
9 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240513082204_scores_unique_id_and_projectid_instead_of_id_and_traceid_index/migration.sql:
--------------------------------------------------------------------------------
1 | /*
2 |   Warnings:
3 | 
4 |   - A unique constraint covering the columns `[id,project_id]` on the table `scores` will be added. If there are existing duplicate values, this will fail.
5 | 
6 | */
7 | -- CreateIndex
8 | CREATE UNIQUE INDEX CONCURRENTLY "scores_id_project_id_key" ON "scores"("id", "project_id");
9 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240522081254_scores_add_author_user_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "scores" ADD COLUMN     "author_user_id" TEXT;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240522095738_scores_add_author_user_id_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "scores_author_user_id_idx" ON "scores"("author_user_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240523142524_scores_add_config_id_idx/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "scores_config_id_idx" ON "scores"("config_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240523142610_scores_add_fk_scores_config_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- AddForeignKey
2 | ALTER TABLE "scores" ADD CONSTRAINT "scores_config_id_fkey" FOREIGN KEY ("config_id") REFERENCES "score_configs"("id") ON DELETE SET NULL ON UPDATE CASCADE;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240524154058_scores_source_enum_add_annotation/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterEnum
2 | ALTER TYPE "ScoreSource" ADD VALUE 'ANNOTATION';
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240524156058_scores_source_backfill_annotation_for_review/migration.sql:
--------------------------------------------------------------------------------
1 | -- Backfill the scores source for 'REVIEW' to be 'ANNOTATION'
2 | UPDATE "scores"
3 | SET "source" = 'ANNOTATION'::"ScoreSource"
4 | WHERE "source" = 'REVIEW'::"ScoreSource";
5 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240524165931_scores_source_enum_drop_review/migration.sql:
--------------------------------------------------------------------------------
 1 | /*
 2 |   Warnings:
 3 | 
 4 |   - The values [REVIEW] on the enum `ScoreSource` will be removed. If these variants are still used in the database, this will fail.
 5 | 
 6 | */
 7 | -- AlterEnum
 8 | BEGIN;
 9 | CREATE TYPE "ScoreSource_new" AS ENUM ('ANNOTATION', 'API', 'EVAL');
10 | ALTER TABLE "scores" ALTER COLUMN "source" TYPE "ScoreSource_new" USING ("source"::text::"ScoreSource_new");
11 | ALTER TYPE "ScoreSource" RENAME TO "ScoreSource_old";
12 | ALTER TYPE "ScoreSource_new" RENAME TO "ScoreSource";
13 | DROP TYPE "ScoreSource_old";
14 | COMMIT;
15 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240524190433_job_executions_add_fk_index_config_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "job_executions_job_configuration_id_idx" ON "job_executions"("job_configuration_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240524190434_job_executions_add_fk_index_score_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "job_executions_job_output_score_id_idx" ON "job_executions"("job_output_score_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240524190435_job_executions_add_fk_index_trace_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "job_executions_job_input_trace_id_idx" ON "job_executions"("job_input_trace_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240524190436_job_executions_index_created_at/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "job_executions_created_at_idx" ON "job_executions"("created_at");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214726_add_cursor_new_columns_observations/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "observations" ADD COLUMN     "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214727_add_cursor_new_columns_scores/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- AlterTable
3 | ALTER TABLE "scores" ADD COLUMN     "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
4 | ADD COLUMN     "updated_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP;
5 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_01/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "audit_logs_updated_at_idx" ON "audit_logs"("updated_at");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_02/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "dataset_items_created_at_idx" ON "dataset_items"("created_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_03/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "dataset_items_updated_at_idx" ON "dataset_items"("updated_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_04/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "dataset_run_items_created_at_idx" ON "dataset_run_items"("created_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_05/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "dataset_run_items_updated_at_idx" ON "dataset_run_items"("updated_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_06/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "dataset_runs_created_at_idx" ON "dataset_runs"("created_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_07/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "dataset_runs_updated_at_idx" ON "dataset_runs"("updated_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_08/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "datasets_created_at_idx" ON "datasets"("created_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_09/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "datasets_updated_at_idx" ON "datasets"("updated_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_10/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "job_executions_updated_at_idx" ON "job_executions"("updated_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_11/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "observations_updated_at_idx" ON "observations"("updated_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_12/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "prompts_created_at_idx" ON "prompts"("created_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_13/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "prompts_updated_at_idx" ON "prompts"("updated_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_14/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "score_configs_created_at_idx" ON "score_configs"("created_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_15/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "score_configs_updated_at_idx" ON "score_configs"("updated_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_16/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "scores_created_at_idx" ON "scores"("created_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_17/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "scores_updated_at_idx" ON "scores"("updated_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240528214728_add_cursor_index_18/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- CreateIndex
3 | CREATE INDEX CONCURRENTLY "trace_sessions_updated_at_idx" ON "trace_sessions"("updated_at");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240603212024_dataset_items_add_index_source_trace_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "dataset_items_source_trace_id_idx" ON "dataset_items" USING HASH ("source_trace_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240604133338_scores_add_index_name/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX "scores_project_id_name_idx" ON "scores"("project_id", "name");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240604133339_score_data_type_add_boolean/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterEnum
2 | ALTER TYPE "ScoreDataType" ADD VALUE 'BOOLEAN';
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240606093356_drop_unused_pricings_table/migration.sql:
--------------------------------------------------------------------------------
 1 | /*
 2 |   Warnings:
 3 | 
 4 |   - You are about to drop the `pricings` table. If the table is not empty, all the data it contains will be lost.
 5 | 
 6 | */
 7 | -- DropTable
 8 | DROP TABLE "pricings";
 9 | 
10 | -- DropEnum
11 | DROP TYPE "PricingUnit";
12 | 
13 | -- DropEnum
14 | DROP TYPE "TokenType";
15 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240606133011_remove_trace_fkey_datasetrunitems/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropForeignKey
2 | ALTER TABLE "dataset_run_items" DROP CONSTRAINT "dataset_run_items_trace_id_fkey";
3 | ALTER TABLE "dataset_run_items" DROP CONSTRAINT "dataset_run_items_observation_id_fkey";
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240607212419_model_price_anthropic_via_google_vertex/migration.sql:
--------------------------------------------------------------------------------
1 | -- Google Vertex uses @ to separate model name and version
2 | 
3 | UPDATE "models" SET "match_pattern" = '(?i)^(claude-3-haiku(-|@)?20240307)
#39; WHERE "id" = 'cltr0w45b000008k1407o9qv1';
4 | 
5 | UPDATE "models" SET "match_pattern" = '(?i)^(claude-3-opus(-|@)?20240229)
#39; WHERE "id" = 'cltgy0iuw000008le3vod1hhy';
6 | 
7 | UPDATE "models" SET "match_pattern" = '(?i)^(claude-3-sonnet(-|@)?20240229)
#39; WHERE "id" = 'cltgy0pp6000108le56se7bl3';


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240612101858_add_index_observations_project_id_prompt_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "observations_project_id_prompt_id_idx" ON "observations"("project_id", "prompt_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240617094803_observations_remove_prompt_fk_constraint/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropForeignKey
2 | ALTER TABLE "observations" DROP CONSTRAINT "observations_prompt_id_fkey";
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240618164950_drop_observations_parent_observation_id_idx/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | DROP INDEX CONCURRENTLY IF EXISTS "observations_parent_observation_id_idx";
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240618164951_drop_observations_updated_at_idx/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | DROP INDEX CONCURRENTLY IF EXISTS "observations_updated_at_idx";
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240618164952_drop_scores_updated_at_idx/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | DROP INDEX CONCURRENTLY IF EXISTS "scores_updated_at_idx";
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240618164953_drop_traces_external_id_idx/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | DROP INDEX CONCURRENTLY IF EXISTS "traces_external_id_idx";
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240618164954_drop_traces_release_idx/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | DROP INDEX CONCURRENTLY IF EXISTS "traces_release_idx";
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240618164955_drop_traces_updated_at_idx/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | DROP INDEX CONCURRENTLY IF EXISTS "traces_updated_at_idx";
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240618164956_create_traces_project_id_timestamp_idx/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY "traces_project_id_timestamp_idx" ON "traces"("project_id", "timestamp");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240624133412_models_add_anthropic_3_5_sonnet/migration.sql:
--------------------------------------------------------------------------------
 1 | INSERT INTO models (
 2 |   id,
 3 |   project_id,
 4 |   model_name,
 5 |   match_pattern,
 6 |   start_date,
 7 |   input_price,
 8 |   output_price,
 9 |   total_price,
10 |   unit,
11 |   tokenizer_id
12 | )
13 | VALUES
14 |   -- add 3.5 sonnet model
15 |   ('clxt0n0m60000pumz1j5b7zsf', NULL, 'claude-3-5-sonnet-20240620', '(?i)^(claude-3-5-sonnet(-|@)?20240620)
#39;, NULL, 0.000003, 0.000015, NULL, 'TOKENS', 'claude')


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240625103957_observations_add_calculated_cost_columns/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "observations" ADD COLUMN     "calculated_input_cost" DECIMAL(65,30),
3 | ADD COLUMN     "calculated_output_cost" DECIMAL(65,30),
4 | ADD COLUMN     "calculated_total_cost" DECIMAL(65,30),
5 | ADD COLUMN     "internal_model_id" TEXT;
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240625103958_fix_model_match_gpt4_vision/migration.sql:
--------------------------------------------------------------------------------
 1 | /*
 2 | Previously, the pattern did not allow for model specifications like "1106" or any other 4-digit block. 
 3 | This led to missing models on the generation-update call where the exact model name that was used was provided (including the 4-digit block).
 4 | The new pattern allows for:
 5 | 
 6 | - "gpt-4-vision-preview" as set on generation-create
 7 | - "gpt-4-1106-vision-preview" as set on generation-update
 8 | 
 9 | */
10 | 
11 | UPDATE
12 | 	"models"
13 | SET
14 | 	"match_pattern" = '(?i)^(gpt-4(-\d{4})?-vision-preview)
#39;
15 | WHERE
16 | 	"id" = 'clrkvx5gp000108juaogs54ea'
17 | 	AND "model_name" = 'gpt-4-turbo-vision';


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240704103901_scores_make_value_optional/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "scores" ALTER COLUMN "value" DROP NOT NULL;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240710114043_score_configs_drop_empty_categories_array_for_numeric_scores/migration.sql:
--------------------------------------------------------------------------------
1 | -- Migration script to update score_configs entries
2 | -- Set categories to NULL where data_type is 'NUMERIC' and categories is an empty array
3 | 
4 | UPDATE score_configs
5 | SET categories = NULL
6 | WHERE data_type = 'NUMERIC' AND categories IS NOT NULL;
7 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240718011733_dataset_runs_add_unique_dataset_id_project_id_name copy/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE UNIQUE INDEX CONCURRENTLY "dataset_runs_dataset_id_project_id_name_key" ON "dataset_runs"("dataset_id", "project_id", "name");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240718011734_dataset_runs_drop_unique_dataset_id_name/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | DROP INDEX CONCURRENTLY "dataset_runs_dataset_id_name_key";


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240807111358_models_add_openai_gpt_4o_2024_08_06/migration.sql:
--------------------------------------------------------------------------------
 1 | 
 2 | INSERT INTO models (
 3 |   id,
 4 |   project_id,
 5 |   model_name,
 6 |   match_pattern,
 7 |   start_date,
 8 |   input_price,
 9 |   output_price,
10 |   total_price,
11 |   unit,
12 |   tokenizer_id,
13 |   tokenizer_config
14 | )
15 | VALUES
16 |   -- gpt-4o-2024-08-06
17 |   ('clzjr85f70000ymmzg7hqffra', NULL, 'gpt-4o-2024-08-06', '(?i)^(gpt-4o-2024-08-06)
#39;, NULL, 0.0000025, 0.000010, NULL, 'TOKENS', 'openai', '{ "tokensPerMessage": 3, "tokensPerName": 1, "tokenizerModel": "gpt-4o" }')
18 |   


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240814223824_model_fix_text_embedding_3_large/migration.sql:
--------------------------------------------------------------------------------
1 | 
2 | -- Fix model name
3 | -- https://github.com/langfuse/langfuse/issues/2688
4 | 
5 | UPDATE models
6 | SET model_name = 'text-embedding-3-large'
7 | WHERE id = 'clruwn76700020al7gp8e4g4l'


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240814233029_dataset_items_drop_fkey_on_traces_and_observations/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropForeignKey
2 | ALTER TABLE "dataset_items" DROP CONSTRAINT "dataset_items_source_observation_id_fkey";
3 | 
4 | -- DropForeignKey
5 | ALTER TABLE "dataset_items" DROP CONSTRAINT "dataset_items_source_trace_id_fkey";
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240913185822_account_add_refresh_token_expires_in/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "Account" ADD COLUMN     "refresh_token_expires_in" INTEGER;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183001_remove_covered_indexes_01/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "traces_project_id_idx"; -- covered by traces_project_id_timestamp_idx
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183002_remove_covered_indexes_02/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "datasets_project_id_idx"; -- covered by datasets_project_id_name_key (unique)
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183003_remove_covered_indexes_03/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "eval_templates_project_id_idx"; -- covered by eval_templates_project_id_id_idx
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183004_remove_covered_indexes_04/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "job_configurations_project_id_idx"; -- covered by job_configurations_project_id_id_idx
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183005_remove_covered_indexes_05/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "job_executions_project_id_idx"; -- covered by job_executions_project_id_id_idx
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183006_remove_covered_indexes_06/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "llm_api_keys_project_id_provider_idx"; -- covered by llm_api_keys_project_id_provider_key (unique)
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183007_remove_covered_indexes_07/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "models_project_id_model_name_idx"; -- covered by models_project_id_model_name_start_date_unit_key (unique)
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183008_remove_covered_indexes_08/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "models_project_id_model_name_start_date_unit_idx"; -- covered by models_project_id_model_name_start_date_unit_key (unique)
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183009_remove_covered_indexes_09/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "observations_project_id_idx"; -- covered by observations_project_id_start_time_type_idx
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183010_remove_covered_indexes_10/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "observations_trace_id_idx"; -- covered by observations_trace_id_project_id_start_time_idx
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183011_remove_covered_indexes_11/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "observations_trace_id_project_id_idx"; -- covered by observations_trace_id_project_id_start_time_idx
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183012_remove_covered_indexes_12/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "organization_memberships_org_id_idx"; -- covered by organization_memberships_org_id_user_id_key (unique)
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183013_remove_covered_indexes_13/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "posthog_integrations_project_id_idx"; -- covered by posthog_integrations_pkey (unique)
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183014_remove_covered_indexes_14/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "prompts_project_id_idx"; -- covered by prompts_project_id_name_version_key (unique)
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183015_remove_covered_indexes_15/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "prompts_project_id_name_version_idx"; -- covered by prompts_project_id_name_version_key (unique)
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20240917183016_remove_covered_indexes_16/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | -- Removes indexes that are covered by other indexes on the same table, e.g. (project_id) if (project_id, timestamp) exists.
3 | DROP INDEX CONCURRENTLY IF EXISTS "scores_project_id_idx"; -- covered by scores_project_id_name_idx
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20241009042557_auth_add_created_at_for_gitlab/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "Account" ADD COLUMN     "created_at" INTEGER;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20241009110720_scores_add_nullable_queue_id_column/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "scores" ADD COLUMN     "queue_id" TEXT;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20241010120245_llm_keys_add_config/migration.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE "llm_api_keys" ADD COLUMN "config" JSONB;


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20241023110145_update_claude_sonnet_35/migration.sql:
--------------------------------------------------------------------------------
1 | -- https://docs.anthropic.com/en/docs/about-claude/models#model-comparison-table
2 | UPDATE models SET model_name = 'claude-3.5-sonnet-20241022' WHERE id = 'cm2krz1uf000208jjg5653iud';
3 | UPDATE models SET model_name = 'claude-3.5-sonnet-latest' WHERE id = 'cm2ks2vzn000308jjh4ze1w7q';


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20241024111800_add_background_migrations_table/migration.sql:
--------------------------------------------------------------------------------
 1 | -- CreateTable
 2 | CREATE TABLE "background_migrations" (
 3 |     "id" TEXT NOT NULL,
 4 |     "name" TEXT NOT NULL,
 5 |     "script" TEXT NOT NULL,
 6 |     "args" JSONB NOT NULL,
 7 | 
 8 |     "finished_at" TIMESTAMP(3),
 9 |     "failed_at" TIMESTAMP(3),
10 |     "failed_reason" TEXT,
11 |     "worker_id" TEXT,
12 |     "locked_at" TIMESTAMP(3),
13 | 
14 |     CONSTRAINT "background_migrations_pkey" PRIMARY KEY ("id")
15 | );
16 | 
17 | -- CreateIndex
18 | CREATE UNIQUE INDEX "background_migrations_name_key" ON "background_migrations"("name");
19 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20241024121500_add_generations_cost_backfill_background_migration/migration.sql:
--------------------------------------------------------------------------------
1 | INSERT INTO background_migrations (id, name, script, args)
2 | VALUES ('32859a35-98f5-4a4a-b438-ebc579349e00', '20241024_1216_add_generations_cost_backfill', 'addGenerationsCostBackfill', '{}');
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20241024173000_add_traces_pg_to_ch_background_migration/migration.sql:
--------------------------------------------------------------------------------
1 | INSERT INTO background_migrations (id, name, script, args)
2 | VALUES ('5960f22a-748f-480c-b2f3-bc4f9d5d84bc', '20241024_1730_migrate_traces_from_pg_to_ch', 'migrateTracesFromPostgresToClickhouse', '{}');
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20241024173700_add_observations_pg_to_ch_background_migration/migration.sql:
--------------------------------------------------------------------------------
1 | INSERT INTO background_migrations (id, name, script, args)
2 | VALUES ('7526e7c9-0026-4595-af2c-369dfd9176ec', '20241024_1737_migrate_observations_from_pg_to_ch', 'migrateObservationsFromPostgresToClickhouse', '{}');
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20241024173800_add_scores_pg_to_ch_background_migration/migration.sql:
--------------------------------------------------------------------------------
1 | INSERT INTO background_migrations (id, name, script, args)
2 | VALUES ('94e50334-50d3-4e49-ad2e-9f6d92c85ef7', '20241024_1738_migrate_scores_from_pg_to_ch', 'migrateScoresFromPostgresToClickhouse', '{}');
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20241029130802_prices_drop_excess_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | DROP INDEX CONCURRENTLY "prices_model_id_idx";
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20241104111600_background_migrations_add_state_column/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "background_migrations" ADD COLUMN "state" jsonb NOT NULL DEFAULT '{}';


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20241114175010_job_executions_add_observation_dataset_item_cols/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropForeignKey
2 | ALTER TABLE "job_executions" DROP CONSTRAINT "job_executions_job_input_trace_id_fkey";
3 | 
4 | -- AlterTable
5 | ALTER TABLE "job_executions" ADD COLUMN     "job_input_dataset_item_id" TEXT,
6 | ADD COLUMN     "job_input_observation_id" TEXT;
7 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20241124115100_add_projects_deleted_at/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "projects" ADD COLUMN "deleted_at" TIMESTAMP(3);
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20241206115829_remove_trace_score_observation_constraints/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropForeignKey
2 | ALTER TABLE "job_executions" DROP CONSTRAINT "job_executions_job_output_score_id_fkey";
3 | 
4 | -- DropForeignKey
5 | ALTER TABLE "traces" DROP CONSTRAINT "traces_session_id_project_id_fkey";
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250108220721_add_queue_backup_table/migration.sql:
--------------------------------------------------------------------------------
 1 | -- CreateTable
 2 | CREATE TABLE "queue_backups" (
 3 |     "id" TEXT NOT NULL,
 4 |     "project_id" TEXT,
 5 |     "queue_name" TEXT NOT NULL,
 6 |     "content" JSONB NOT NULL,
 7 |     "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
 8 | 
 9 |     CONSTRAINT "queue_backups_pkey" PRIMARY KEY ("id")
10 | );
11 | 
12 | -- AddForeignKey
13 | ALTER TABLE "traces" ADD CONSTRAINT "traces_session_id_project_id_fkey" FOREIGN KEY ("session_id", "project_id") REFERENCES "trace_sessions"("id", "project_id") ON DELETE RESTRICT ON UPDATE CASCADE;
14 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250109083346_drop_trace_tracesession_fk/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropForeignKey
2 | ALTER TABLE "traces" DROP CONSTRAINT "traces_session_id_project_id_fkey";
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250122152102_add_llm_api_keys_extra_headers/migration.sql:
--------------------------------------------------------------------------------
1 | ALTER TABLE "llm_api_keys"
2 |     ADD COLUMN "extra_headers" TEXT,
3 |     ADD COLUMN "extra_header_keys" TEXT[] NOT NULL DEFAULT '{}'::TEXT[];
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250123103200_add_retention_days_to_projects/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "projects"
3 |     ADD COLUMN "retention_days" INTEGER;
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250128144418_llm_adapter_rename_google_vertex_ai/migration.sql:
--------------------------------------------------------------------------------
1 | UPDATE "llm_api_keys" SET adapter = 'google-vertex-ai' WHERE adapter = 'vertex-ai';
2 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250128163035_add_nullable_commit_message_prompts/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "prompts" ADD COLUMN     "commit_message" TEXT;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250211102600_drop_event_log_table/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropTable
2 | DROP TABLE event_log;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250211123300_drop_events_table/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropTable
2 | DROP TABLE events;
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250214173309_add_timescope_to_configs/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "job_configurations" ADD COLUMN     "time_scope" TEXT[] DEFAULT ARRAY['NEW']::TEXT[];
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250220141500_add_environment_to_trace_sessions/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "trace_sessions"
3 | ADD COLUMN "environment" TEXT NOT NULL DEFAULT 'default';
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250221143400_drop_trace_view_observation_view/migration.sql:
--------------------------------------------------------------------------------
1 | DROP VIEW IF EXISTS "observations_view";
2 | DROP VIEW IF EXISTS "traces_view";


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250310100328_add_api_key_to_audit_log/migration.sql:
--------------------------------------------------------------------------------
 1 | -- CreateEnum
 2 | CREATE TYPE "AuditLogRecordType" AS ENUM ('USER', 'API_KEY');
 3 | 
 4 | -- AlterTable
 5 | ALTER TABLE "audit_logs" ADD COLUMN     "api_key_id" TEXT,
 6 | ADD COLUMN     "type" "AuditLogRecordType" NOT NULL DEFAULT 'USER',
 7 | ALTER COLUMN "user_id" DROP NOT NULL,
 8 | ALTER COLUMN "user_org_role" DROP NOT NULL;
 9 | 
10 | -- CreateIndex
11 | CREATE INDEX "audit_logs_api_key_id_idx" ON "audit_logs"("api_key_id");
12 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250321102240_drop_queue_backup_table/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropTable
2 | DROP TABLE "queue_backups";
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250402142320_add_blobstorage_integration_file_type/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateEnum
2 | CREATE TYPE "BlobStorageIntegrationFileType" AS ENUM ('JSON', 'CSV', 'JSONL');
3 | 
4 | -- AlterTable
5 | ALTER TABLE "blob_storage_integrations" ADD COLUMN     "file_type" "BlobStorageIntegrationFileType" NOT NULL DEFAULT 'CSV';
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250403153555_membership_invitations_no_duplicates/migration.sql:
--------------------------------------------------------------------------------
 1 | -- Delete duplicate membership invitations, keeping only the newest one for each email and org_id combination
 2 | WITH ranked_invitations AS (
 3 |   SELECT 
 4 |     id,
 5 |     email,
 6 |     org_id,
 7 |     ROW_NUMBER() OVER (PARTITION BY email, org_id ORDER BY updated_at DESC) as rn
 8 |   FROM membership_invitations
 9 | )
10 | DELETE FROM membership_invitations
11 | WHERE id IN (
12 |   SELECT id FROM ranked_invitations WHERE rn > 1
13 | );
14 | 
15 | 
16 | -- CreateIndex
17 | CREATE UNIQUE INDEX "membership_invitations_email_org_id_key" ON "membership_invitations"("email", "org_id");
18 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250410145712_add_organization_scoped_api_keys/migration.sql:
--------------------------------------------------------------------------------
 1 | -- CreateEnum
 2 | CREATE TYPE "ApiKeyScope" AS ENUM ('ORGANIZATION', 'PROJECT');
 3 | 
 4 | -- AlterTable
 5 | ALTER TABLE "api_keys" ADD COLUMN     "organization_id" TEXT,
 6 | ADD COLUMN     "scope" "ApiKeyScope" NOT NULL DEFAULT 'PROJECT',
 7 | ALTER COLUMN "project_id" DROP NOT NULL;
 8 | 
 9 | -- CreateIndex
10 | CREATE INDEX "api_keys_organization_id_idx" ON "api_keys"("organization_id");
11 | 
12 | -- AddForeignKey
13 | ALTER TABLE "api_keys" ADD CONSTRAINT "api_keys_organization_id_fkey" FOREIGN KEY ("organization_id") REFERENCES "organizations"("id") ON DELETE CASCADE ON UPDATE CASCADE;
14 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250420120553_add_organization_and_project_metadata/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "organizations" ADD COLUMN     "metadata" JSONB;
3 | 
4 | -- AlterTable
5 | ALTER TABLE "projects" ADD COLUMN     "metadata" JSONB;
6 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250517173700_add_event_log_migration_background_migration.sql/migration.sql:
--------------------------------------------------------------------------------
1 | INSERT INTO background_migrations (id, name, script, args)
2 | VALUES ('c19b91d9-f9a2-468b-8209-95578f970c5b', '20250417_1737_migrate_event_log_to_blob_storage', 'migrateEventLogToBlobStorageRefTable', '{}');
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250519073249_add_trace_media_media_id_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY IF NOT EXISTS "trace_media_project_id_media_id_idx" ON "trace_media"("project_id", "media_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250519073327_add_observation_media_media_id_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- CreateIndex
2 | CREATE INDEX CONCURRENTLY IF NOT EXISTS "observation_media_project_id_media_id_idx" ON "observation_media"("project_id", "media_id");
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250519093327_media_add_index_project_id_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- Index cannot be created concurrently in a transaction, so we need to create it separately
2 | -- Prerequisite for migration 20250518075613_media_relax_id_uniqueness_to_project_only
3 | CREATE UNIQUE INDEX CONCURRENTLY IF NOT EXISTS "media_project_id_id_key" ON "media"("project_id", "id");
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250520123737_add_single_aggregate_chart_type/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterEnum
2 | ALTER TYPE "DashboardWidgetChartType" ADD VALUE 'NUMBER';
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250522140357_remove_obsolete_observation_media_index/migration.sql:
--------------------------------------------------------------------------------
1 | -- DropIndex
2 | DROP INDEX CONCURRENTLY IF EXISTS "observation_media_project_id_observation_id_idx";
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250523110540_modify_nullable_cols_eval_templates/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "eval_templates" ALTER COLUMN "project_id" DROP NOT NULL;
3 | ALTER TABLE "eval_templates" ALTER COLUMN "model" DROP NOT NULL;
4 | ALTER TABLE "eval_templates" ALTER COLUMN "provider" DROP NOT NULL;
5 | ALTER TABLE "eval_templates" ALTER COLUMN "model_params" DROP NOT NULL;
6 | ALTER TABLE "eval_templates" ADD COLUMN "partner" TEXT;


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250523120545_add_nullable_job_template_id/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "job_executions" ADD COLUMN "job_template_id" TEXT;
3 | ALTER TABLE "job_executions" ADD CONSTRAINT "job_executions_job_template_id_fkey" FOREIGN KEY ("job_template_id") REFERENCES "eval_templates"("id") ON DELETE SET NULL;
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250529071241_make_blobstorage_integration_credentials_optional/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterTable
2 | ALTER TABLE "blob_storage_integrations" ALTER COLUMN "access_key_id" DROP NOT NULL,
3 | ALTER COLUMN "secret_access_key" DROP NOT NULL;
4 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/20250604085536_add_histogram_chart_type/migration.sql:
--------------------------------------------------------------------------------
1 | -- AlterEnum
2 | ALTER TYPE "DashboardWidgetChartType" ADD VALUE 'HISTOGRAM';
3 | 


--------------------------------------------------------------------------------
/packages/shared/prisma/migrations/migration_lock.toml:
--------------------------------------------------------------------------------
1 | # Please do not edit this file manually
2 | # It should be added in your version-control system (e.g., Git)
3 | provider = "postgresql"


--------------------------------------------------------------------------------
/packages/shared/scripts/cleanup.sql:
--------------------------------------------------------------------------------
1 | DO $
2 | BEGIN
3 |  IF EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = '_prisma_migrations') THEN
4 |   DELETE FROM _prisma_migrations
5 |   WHERE migration_name IN ('20240606090858_pricings_add_latest_gemini_models', '20240530212419_model_price_anthropic_via_google_vertex', '20240604133340_backfill_manual_scores');
6 |  END IF;
7 | END $;


--------------------------------------------------------------------------------
/packages/shared/src/constants.ts:
--------------------------------------------------------------------------------
 1 | /* eslint-disable no-unused-vars */
 2 | // disable lint as this is exported and used in packages
 3 | export enum ModelUsageUnit {
 4 |   Characters = "CHARACTERS",
 5 |   Tokens = "TOKENS",
 6 |   Seconds = "SECONDS",
 7 |   Milliseconds = "MILLISECONDS",
 8 |   Images = "IMAGES",
 9 |   Requests = "REQUESTS",
10 | }
11 | 


--------------------------------------------------------------------------------
/packages/shared/src/domain/index.ts:
--------------------------------------------------------------------------------
1 | export * from "./observations";
2 | export * from "./traces";
3 | export * from "./scores";
4 | export * from "./table-view-presets";
5 | 


--------------------------------------------------------------------------------
/packages/shared/src/errors/ApiError.ts:
--------------------------------------------------------------------------------
1 | import { BaseError } from "./BaseError";
2 | 
3 | export class ApiError extends BaseError {
4 |   constructor(description = "Api call failed", status = 500) {
5 |     super("ApiError", status, description, true);
6 |   }
7 | }
8 | 


--------------------------------------------------------------------------------
/packages/shared/src/errors/BaseError.ts:
--------------------------------------------------------------------------------
 1 | export class BaseError extends Error {
 2 |   public readonly name: string;
 3 |   public readonly httpCode: number;
 4 |   public readonly isOperational: boolean;
 5 | 
 6 |   constructor(
 7 |     name: string,
 8 |     httpCode: number,
 9 |     description: string,
10 |     isOperational: boolean
11 |   ) {
12 |     super(description);
13 |     Object.setPrototypeOf(this, new.target.prototype); // restore prototype chain
14 | 
15 |     this.name = name;
16 |     this.httpCode = httpCode;
17 |     this.isOperational = isOperational; // if error is part of known errors that our application can anticipate
18 | 
19 |     Error.captureStackTrace(this);
20 |   }
21 | }
22 | 


--------------------------------------------------------------------------------
/packages/shared/src/errors/ConflictError.ts:
--------------------------------------------------------------------------------
1 | import { BaseError } from "./BaseError";
2 | 
3 | export class LangfuseConflictError extends BaseError {
4 |   constructor(description = "Conflict") {
5 |     super("LangfuseConflictError", 409, description, true);
6 |   }
7 | }
8 | 


--------------------------------------------------------------------------------
/packages/shared/src/errors/ForbiddenError.ts:
--------------------------------------------------------------------------------
1 | import { BaseError } from "./BaseError";
2 | 
3 | export class ForbiddenError extends BaseError {
4 |   constructor(description = "Forbidden") {
5 |     super("ForbiddenError", 403, description, true);
6 |   }
7 | }
8 | 


--------------------------------------------------------------------------------
/packages/shared/src/errors/InternalServerError.ts:
--------------------------------------------------------------------------------
1 | import { BaseError } from "./BaseError";
2 | 
3 | export class InternalServerError extends BaseError {
4 |   constructor(description = "Internal Server Error") {
5 |     super("InternalServerError", 500, description, true);
6 |   }
7 | }
8 | 


--------------------------------------------------------------------------------
/packages/shared/src/errors/InvalidRequestError.ts:
--------------------------------------------------------------------------------
1 | import { BaseError } from "./BaseError";
2 | 
3 | export class InvalidRequestError extends BaseError {
4 |   constructor(description = "Invalid Request Error") {
5 |     super("InvalidRequestError", 400, description, true);
6 |   }
7 | }
8 | 


--------------------------------------------------------------------------------
/packages/shared/src/errors/MethodNotAllowedError.ts:
--------------------------------------------------------------------------------
1 | import { BaseError } from "./BaseError";
2 | 
3 | export class MethodNotAllowedError extends BaseError {
4 |   constructor(description = "Method not allowed") {
5 |     super("MethodNotAllowedError", 405, description, true);
6 |   }
7 | }
8 | 


--------------------------------------------------------------------------------
/packages/shared/src/errors/NotFoundError.ts:
--------------------------------------------------------------------------------
1 | import { BaseError } from "./BaseError";
2 | 
3 | export class LangfuseNotFoundError extends BaseError {
4 |   constructor(description = "Not Found") {
5 |     super("LangfuseNotFoundError", 404, description, true);
6 |   }
7 | }
8 | 


--------------------------------------------------------------------------------
/packages/shared/src/errors/UnauthorizedError.ts:
--------------------------------------------------------------------------------
1 | import { BaseError } from "./BaseError";
2 | 
3 | export class UnauthorizedError extends BaseError {
4 |   constructor(description = "Unauthorized") {
5 |     super("UnauthorizedError", 401, description, true);
6 |   }
7 | }
8 | 


--------------------------------------------------------------------------------
/packages/shared/src/errors/index.ts:
--------------------------------------------------------------------------------
 1 | export { BaseError } from "./BaseError";
 2 | export { LangfuseNotFoundError } from "./NotFoundError";
 3 | export { InvalidRequestError } from "./InvalidRequestError";
 4 | export { UnauthorizedError } from "./UnauthorizedError";
 5 | export { ForbiddenError } from "./ForbiddenError";
 6 | export { MethodNotAllowedError } from "./MethodNotAllowedError";
 7 | export { ApiError } from "./ApiError";
 8 | export { InternalServerError } from "./InternalServerError";
 9 | export { LangfuseConflictError } from "./ConflictError";
10 | 


--------------------------------------------------------------------------------
/packages/shared/src/features/comments/types.ts:
--------------------------------------------------------------------------------
 1 | import { z } from "zod/v4";
 2 | 
 3 | const MAX_COMMENT_LENGTH = 3000;
 4 | 
 5 | const COMMENT_OBJECT_TYPES = [
 6 |   "TRACE",
 7 |   "OBSERVATION",
 8 |   "SESSION",
 9 |   "PROMPT",
10 | ] as const;
11 | 
12 | export const CreateCommentData = z.object({
13 |   projectId: z.string(),
14 |   content: z.string().trim().min(1).max(MAX_COMMENT_LENGTH),
15 |   objectId: z.string(),
16 |   objectType: z.enum(COMMENT_OBJECT_TYPES),
17 | });
18 | 
19 | export const DeleteCommentData = z.object({
20 |   projectId: z.string(),
21 |   commentId: z.string(),
22 |   objectId: z.string(),
23 |   objectType: z.enum(COMMENT_OBJECT_TYPES),
24 | });
25 | 


--------------------------------------------------------------------------------
/packages/shared/src/features/experiments/utils.ts:
--------------------------------------------------------------------------------
 1 | import { Prisma } from "../../db";
 2 | 
 3 | export const datasetItemMatchesVariable = (
 4 |   input: Prisma.JsonValue,
 5 |   variable: string,
 6 | ) => {
 7 |   if (
 8 |     input === null ||
 9 |     input === undefined ||
10 |     typeof input !== "object" ||
11 |     Array.isArray(input)
12 |   )
13 |     return false;
14 |   return Object.keys(input).includes(variable);
15 | };
16 | 


--------------------------------------------------------------------------------
/packages/shared/src/features/scores/index.ts:
--------------------------------------------------------------------------------
1 | export * from "./interfaces";
2 | export * from "./scoreConfigTypes";
3 | 


--------------------------------------------------------------------------------
/packages/shared/src/features/scores/interfaces/api/index.ts:
--------------------------------------------------------------------------------
1 | export * from "./v1/schemas";
2 | export * from "./v1/validation";
3 | export * from "./v1/endpoints";
4 | export * from "./v2/schemas";
5 | export * from "./v2/validation";
6 | export * from "./v2/endpoints";
7 | 


--------------------------------------------------------------------------------
/packages/shared/src/features/scores/interfaces/index.ts:
--------------------------------------------------------------------------------
1 | export * from "./api";
2 | export * from "./application/validation";
3 | export * from "./ingestion/validation";
4 | export * from "./ui/types";
5 | 


--------------------------------------------------------------------------------
/packages/shared/src/interfaces/orderBy.ts:
--------------------------------------------------------------------------------
 1 | import { z } from "zod/v4";
 2 | 
 3 | export const orderBy = z
 4 |   .object({
 5 |     column: z.string(),
 6 |     order: z.enum(["ASC", "DESC"]),
 7 |   })
 8 |   .nullable();
 9 | 
10 | export type OrderByState = z.infer<typeof orderBy>;
11 | 


--------------------------------------------------------------------------------
/packages/shared/src/interfaces/parseDbOrg.ts:
--------------------------------------------------------------------------------
 1 | import { type Organization } from "@prisma/client";
 2 | import { CloudConfigSchema } from "./cloudConfigSchema";
 3 | 
 4 | type parsedOrg = Omit<Organization, "cloudConfig"> & {
 5 |   cloudConfig: CloudConfigSchema | null;
 6 | };
 7 | 
 8 | export function parseDbOrg(dbOrg: Organization): parsedOrg {
 9 |   const { cloudConfig, ...org } = dbOrg;
10 | 
11 |   const parsedCloudConfig = CloudConfigSchema.safeParse(cloudConfig);
12 | 
13 |   const parsedOrg = {
14 |     ...org,
15 |     cloudConfig: parsedCloudConfig.success ? parsedCloudConfig.data : null,
16 |   };
17 | 
18 |   return parsedOrg;
19 | }
20 | 


--------------------------------------------------------------------------------
/packages/shared/src/interfaces/search.ts:
--------------------------------------------------------------------------------
1 | import { z } from "zod/v4";
2 | 
3 | export const TracingSearchType = z.enum(["id", "content"]);
4 | // id: for searching smaller columns like IDs, types, and other metadata
5 | // content: for searching input/output text of functions traced via OpenTelemetry
6 | export type TracingSearchType = z.infer<typeof TracingSearchType>;
7 | 


--------------------------------------------------------------------------------
/packages/shared/src/interfaces/tableNames.ts:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * Shared table names used across batch operations (exports, actions, etc.)
 3 |  * This enum provides a centralized definition of database table names
 4 |  * to avoid coupling between different batch operation types.
 5 |  */
 6 | export enum BatchTableNames {
 7 |   Scores = "scores",
 8 |   Sessions = "sessions",
 9 |   Traces = "traces",
10 |   Observations = "observations",
11 |   DatasetRunItems = "dataset_run_items",
12 |   AuditLogs = "audit_logs",
13 | }
14 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/clickhouse/schema.ts:
--------------------------------------------------------------------------------
 1 | export const ClickhouseTableNames = {
 2 |   traces: "traces",
 3 |   observations: "observations",
 4 |   scores: "scores",
 5 | 
 6 |   // Virtual tables for dashboards
 7 |   // TODO: Check if we can do this more elegantly
 8 |   scores_numeric: "scores_numeric",
 9 |   scores_categorical: "scores_categorical",
10 | } as const;
11 | 
12 | export type ClickhouseTableName = keyof typeof ClickhouseTableNames;
13 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/llm/utils.ts:
--------------------------------------------------------------------------------
 1 | import { z } from "zod/v4";
 2 | 
 3 | import { decrypt } from "../../encryption";
 4 | 
 5 | const ExtraHeaderSchema = z.record(z.string(), z.string());
 6 | 
 7 | export function decryptAndParseExtraHeaders(
 8 |   extraHeaders: string | null | undefined,
 9 | ) {
10 |   if (!extraHeaders) return;
11 | 
12 |   return ExtraHeaderSchema.parse(JSON.parse(decrypt(extraHeaders)));
13 | }
14 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/queries/createGenerationsQuery.ts:
--------------------------------------------------------------------------------
 1 | import { Observation } from "../../domain";
 2 | 
 3 | type AdditionalObservationFields = {
 4 |   traceName: string | null;
 5 |   traceTags: Array<string>;
 6 |   traceTimestamp: Date | null;
 7 | };
 8 | 
 9 | export type FullObservation = AdditionalObservationFields & Observation;
10 | 
11 | export type FullObservations = Array<FullObservation>;
12 | 
13 | export type FullObservationsWithScores = Array<
14 |   FullObservation & { scores?: Record<string, string[] | number[]> | null }
15 | >;
16 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/queries/types.ts:
--------------------------------------------------------------------------------
 1 | import z from "zod/v4";
 2 | import { singleFilter } from "../../interfaces/filters";
 3 | import { orderBy } from "../../interfaces/orderBy";
 4 | import { optionalPaginationZod } from "../../utils/zod";
 5 | 
 6 | const TableFilterSchema = z.object({
 7 |   projectId: z.string(),
 8 |   filter: z.array(singleFilter).nullish(),
 9 |   searchQuery: z.string().nullish(),
10 |   orderBy: orderBy,
11 |   ...optionalPaginationZod,
12 | });
13 | 
14 | export type TableFilters = z.infer<typeof TableFilterSchema>;
15 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/repositories/constants.ts:
--------------------------------------------------------------------------------
 1 | // Rule of thumb: If you join observations from left, use observations to trace and vice versa
 2 | 
 3 | // t.timestamp > observation.start_time - 2 days
 4 | export const OBSERVATIONS_TO_TRACE_INTERVAL = "INTERVAL 2 DAY";
 5 | // observation.start_time > t.timestamp - 1 hour
 6 | export const TRACE_TO_OBSERVATIONS_INTERVAL = "INTERVAL 1 HOUR";
 7 | // observation.start_time > s.timestamp - 1 hour
 8 | // t.timestamp > s.timestamp - 1 hour
 9 | export const SCORE_TO_TRACE_OBSERVATIONS_INTERVAL = "INTERVAL 1 HOUR";
10 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/repositories/index.ts:
--------------------------------------------------------------------------------
 1 | export * from "./scores";
 2 | export * from "./traces";
 3 | export * from "./observations";
 4 | export * from "./types";
 5 | export * from "./dashboards";
 6 | export * from "./traces_converters";
 7 | export * from "./scores_converters";
 8 | export * from "./observations_converters";
 9 | export * from "./clickhouse";
10 | export * from "./constants";
11 | export * from "./trace-sessions";
12 | export * from "./scores-utils";
13 | export * from "./blobStorageLog";
14 | export * from "./environments";
15 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/repositories/types.ts:
--------------------------------------------------------------------------------
1 | export type TableCount = {
2 |   count: number;
3 | };
4 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/services/DashboardService/index.ts:
--------------------------------------------------------------------------------
1 | export * from "./DashboardService";
2 | export * from "./types";
3 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/services/DefaultEvaluationModelService/index.ts:
--------------------------------------------------------------------------------
1 | export * from "./DefaultEvalModelService";
2 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/services/PromptService/utils.ts:
--------------------------------------------------------------------------------
1 | export function escapeRegex(str: string | number) {
2 |   return String(str).replace(/[.*+?^${}()|[\]\\]/g, "\\
amp;");
3 | }
4 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/services/TableViewService/index.ts:
--------------------------------------------------------------------------------
1 | export * from "./TableViewService";
2 | export * from "./types";
3 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/test-utils/index.ts:
--------------------------------------------------------------------------------
1 | export * from "./tracing-factory";
2 | export * from "./clickhouse-helpers";
3 | export * from "./org-factory";
4 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/utils/metadata_conversion.ts:
--------------------------------------------------------------------------------
 1 | import { parseJsonPrioritised } from "../../utils/json";
 2 | import { MetadataDomain } from "../../domain";
 3 | 
 4 | export function parseMetadataCHRecordToDomain(
 5 |   metadata: Record<string, string>,
 6 | ): MetadataDomain {
 7 |   return metadata
 8 |     ? Object.fromEntries(
 9 |         Object.entries(metadata ?? {}).map(([key, val]) => [
10 |           key,
11 |           val === null ? null : parseJsonPrioritised(val),
12 |         ]),
13 |       )
14 |     : {};
15 | }
16 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/utils/transforms/index.ts:
--------------------------------------------------------------------------------
 1 | import { Transform } from "stream";
 2 | 
 3 | import { BatchExportFileFormat } from "../../../features/batchExport/types";
 4 | import { transformStreamToCsv } from "./transformStreamToCsv";
 5 | import { transformStreamToJson } from "./transformStreamToJson";
 6 | import { transformStreamToJsonl } from "./transformStreamToJsonl";
 7 | 
 8 | export const streamTransformations: Record<
 9 |   BatchExportFileFormat,
10 |   () => Transform
11 | > = {
12 |   CSV: transformStreamToCsv,
13 |   JSON: transformStreamToJson,
14 |   JSONL: transformStreamToJsonl,
15 | };
16 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/utils/transforms/stringify.ts:
--------------------------------------------------------------------------------
1 | export const stringify = (data: any): string => {
2 |   return JSON.stringify(data, (key, value) =>
3 |     typeof value === "bigint" ? Number.parseInt(value.toString()) : value
4 |   );
5 | };
6 | 


--------------------------------------------------------------------------------
/packages/shared/src/server/utils/transforms/transformStreamToJsonl.ts:
--------------------------------------------------------------------------------
 1 | import { Transform, type TransformCallback } from "stream";
 2 | import { stringify } from "./stringify";
 3 | 
 4 | export function transformStreamToJsonl(): Transform {
 5 |   return new Transform({
 6 |     objectMode: true,
 7 | 
 8 |     transform(
 9 |       row: Record<string, any>,
10 |       encoding: BufferEncoding,
11 |       callback: TransformCallback,
12 |     ): void {
13 |       this.push(stringify(row) + "\n");
14 |       callback();
15 |     },
16 |   });
17 | }
18 | 


--------------------------------------------------------------------------------
/packages/shared/src/tableDefinitions/index.ts:
--------------------------------------------------------------------------------
1 | export * from "./sessionsView";
2 | export * from "./types";
3 | export * from "./mapObservationsTable";
4 | export * from "./mapTracesTable";
5 | export * from "./mapDashboards";
6 | export * from "./mapScoresTable";
7 | 


--------------------------------------------------------------------------------
/packages/shared/src/utils/environment.ts:
--------------------------------------------------------------------------------
 1 | // https://github.com/t3-oss/t3-env/blob/e7e21095e00a477e37608783defda5a6a99586d0/packages/core/src/index.ts#L228
 2 | // unfortunately, we are not able to install t3-env in all our packaging as some rely on commonjs.
 3 | export const removeEmptyEnvVariables = (runtimeEnv: any) => {
 4 |   for (const [key, value] of Object.entries(runtimeEnv)) {
 5 |     if (value === "") {
 6 |       delete runtimeEnv[key];
 7 |     }
 8 |   }
 9 |   return runtimeEnv;
10 | };
11 | 


--------------------------------------------------------------------------------
/packages/shared/src/utils/objects.ts:
--------------------------------------------------------------------------------
 1 | type OmitKeys<T, K extends keyof T> = Pick<T, Exclude<keyof T, K>>;
 2 | 
 3 | /**
 4 |  * Removes specified keys from an object and returns a new object without those keys.
 5 |  */
 6 | 
 7 | export function removeObjectKeys<T, K extends keyof T>(
 8 |   obj: T,
 9 |   keys: K[]
10 | ): OmitKeys<T, K> {
11 |   const result = { ...obj };
12 |   for (const key of keys) {
13 |     delete result[key];
14 |   }
15 |   return result;
16 | }
17 | 


--------------------------------------------------------------------------------
/packages/shared/src/utils/typeChecks.ts:
--------------------------------------------------------------------------------
1 | import { z } from "zod/v4";
2 | 
3 | export const isPresent = <T>(value: T | null | undefined): value is T =>
4 |   value !== null && value !== undefined && value !== "";
5 | 
6 | export const stringDateTime = z.string().datetime({ offset: true }).nullish();
7 | 


--------------------------------------------------------------------------------
/packages/shared/tsconfig.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "extends": "@repo/typescript-config/base.json",
 3 |   "compilerOptions": {
 4 |     "jsx": "react",
 5 |     "moduleResolution": "NodeNext",
 6 |     "module": "NodeNext",
 7 |     "lib": ["ES2021"],
 8 |     "outDir": "./dist",
 9 |     "types": ["node"],
10 |     "target": "ES2020",
11 |     "rootDir": "."
12 |   },
13 |   "include": ["."],
14 |   "exclude": ["node_modules", "dist"]
15 | }
16 | 


--------------------------------------------------------------------------------
/pnpm-workspace.yaml:
--------------------------------------------------------------------------------
1 | packages:
2 |   # include packages in subfolders (e.g. apps/ and packages/)
3 |   - "web"
4 |   - "worker"
5 |   - "packages/**"
6 |   - "ee"
7 | 


--------------------------------------------------------------------------------
/scripts/nuke.sh:
--------------------------------------------------------------------------------
 1 | 
 2 | #  used to nuke the dev environment for engineers
 3 | 
 4 | find . -name 'node_modules' -type d -prune -print -exec rm -rf '{}' \;
 5 | find . -name '.next' -type d -prune -print -exec rm -rf '{}' \;
 6 | find . -iname "bin" -type d -prune -print -exec rm -rf '{}' \;
 7 | find . -iname "dist" -type d -prune -print -exec rm -rf '{}' \;
 8 | find . -iname "out" -type d -prune -print -exec rm -rf '{}' \;
 9 | find . -iname ".turbo" -type d -prune -print -exec rm -rf '{}' \;
10 | find . -iname "tsconfig.tsbuildinfo" -type d -prune -print -exec rm -rf '{}' \;
11 | 
12 | pnpm store prune
13 | 


--------------------------------------------------------------------------------
/web/.eslintrc.js:
--------------------------------------------------------------------------------
1 | /** @type {import("eslint").Linter.Config} */
2 | module.exports = {
3 |   extends: ["@repo/eslint-config/next.js"],
4 |   parser: "@typescript-eslint/parser",
5 |   parserOptions: {
6 |     project: true,
7 |   },
8 | };
9 | 


--------------------------------------------------------------------------------
/web/components.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "$schema": "https://ui.shadcn.com/schema.json",
 3 |   "style": "default",
 4 |   "rsc": true,
 5 |   "tailwind": {
 6 |     "config": "tailwind.config.ts",
 7 |     "css": "src/styles/globals.css",
 8 |     "baseColor": "slate",
 9 |     "cssVariables": true
10 |   },
11 |   "aliases": {
12 |     "components": "@/src/components",
13 |     "utils": "@/src/utils/tailwind"
14 |   }
15 | }
16 | 


--------------------------------------------------------------------------------
/web/playwright.config.ts:
--------------------------------------------------------------------------------
 1 | import { defineConfig } from "@playwright/test";
 2 | 
 3 | export default defineConfig({
 4 |   use: {
 5 |     /* Base URL to use in actions like `await page.goto('/')`. */
 6 |     baseURL: "http://localhost:3000",
 7 |   },
 8 |   webServer: {
 9 |     command: process.env.CI ? "npm run start" : "npm run dev",
10 |     url: "http://127.0.0.1:3000",
11 |     reuseExistingServer: !process.env.CI,
12 |     stdout: "ignore",
13 |     stderr: "pipe",
14 |   },
15 | });
16 | 


--------------------------------------------------------------------------------
/web/postcss.config.cjs:
--------------------------------------------------------------------------------
1 | const config = {
2 |   plugins: {
3 |     tailwindcss: {},
4 |     autoprefixer: {},
5 |   },
6 | };
7 | 
8 | module.exports = config;
9 | 


--------------------------------------------------------------------------------
/web/prettier.config.cjs:
--------------------------------------------------------------------------------
1 | /** @type {import("prettier").Config} */
2 | const config = {
3 |   plugins: [require.resolve("prettier-plugin-tailwindcss")],
4 | };
5 | 
6 | module.exports = config;
7 | 


--------------------------------------------------------------------------------
/web/public/android-chrome-192x192.png:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langfuse/langfuse/c8b282dc822c8cec556663f25a000eee58c0dbf6/web/public/android-chrome-192x192.png


--------------------------------------------------------------------------------
/web/public/apple-touch-icon.png:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langfuse/langfuse/c8b282dc822c8cec556663f25a000eee58c0dbf6/web/public/apple-touch-icon.png


--------------------------------------------------------------------------------
/web/public/assets/ragas-logo.png:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langfuse/langfuse/c8b282dc822c8cec556663f25a000eee58c0dbf6/web/public/assets/ragas-logo.png


--------------------------------------------------------------------------------
/web/public/favicon-16x16.png:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langfuse/langfuse/c8b282dc822c8cec556663f25a000eee58c0dbf6/web/public/favicon-16x16.png


--------------------------------------------------------------------------------
/web/public/favicon-32x32.png:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langfuse/langfuse/c8b282dc822c8cec556663f25a000eee58c0dbf6/web/public/favicon-32x32.png


--------------------------------------------------------------------------------
/web/public/favicon.ico:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langfuse/langfuse/c8b282dc822c8cec556663f25a000eee58c0dbf6/web/public/favicon.ico


--------------------------------------------------------------------------------
/web/public/icon256.png:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langfuse/langfuse/c8b282dc822c8cec556663f25a000eee58c0dbf6/web/public/icon256.png


--------------------------------------------------------------------------------
/web/src/__tests__/after-teardown.ts:
--------------------------------------------------------------------------------
1 | import teardown from "@/src/__tests__/teardown";
2 | 
3 | afterAll(async () => {
4 |   await teardown();
5 | });
6 | 


--------------------------------------------------------------------------------
/web/src/__tests__/static/bitcoin.pdf:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langfuse/langfuse/c8b282dc822c8cec556663f25a000eee58c0dbf6/web/src/__tests__/static/bitcoin.pdf


--------------------------------------------------------------------------------
/web/src/__tests__/static/langfuse-logo.png:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/langfuse/langfuse/c8b282dc822c8cec556663f25a000eee58c0dbf6/web/src/__tests__/static/langfuse-logo.png


--------------------------------------------------------------------------------
/web/src/__tests__/teardown.ts:
--------------------------------------------------------------------------------
 1 | export default async function teardown() {
 2 |   const { redis, logger } = await import("@langfuse/shared/src/server");
 3 |   logger.debug(`Redis status ${redis?.status}`);
 4 |   if (!redis) {
 5 |     return;
 6 |   }
 7 |   if (redis.status === "end" || redis.status === "close") {
 8 |     logger.debug("Redis connection already closed");
 9 |     return;
10 |   }
11 |   redis?.disconnect();
12 |   logger.debug("Teardown complete");
13 | }
14 | 


--------------------------------------------------------------------------------
/web/src/app/api/billing/stripe-webhook/route.ts:
--------------------------------------------------------------------------------
1 | import { stripeWebhookApiHandler } from "@/src/ee/features/billing/server/stripeWebhookApiHandler";
2 | 
3 | export const dynamic = "force-dynamic";
4 | 
5 | export const POST = stripeWebhookApiHandler;
6 | 


--------------------------------------------------------------------------------
/web/src/app/api/chatCompletion/route.ts:
--------------------------------------------------------------------------------
1 | import chatCompletionHandler from "@/src/features/playground/server/chatCompletionHandler";
2 | 
3 | export const dynamic = "force-dynamic";
4 | export const maxDuration = 120;
5 | 
6 | export const POST = chatCompletionHandler;
7 | 


--------------------------------------------------------------------------------
/web/src/app/layout.tsx:
--------------------------------------------------------------------------------
 1 | export const metadata = {
 2 |   title: 'Next.js',
 3 |   description: 'Generated by Next.js',
 4 | }
 5 | 
 6 | export default function RootLayout({
 7 |   children,
 8 | }: {
 9 |   children: React.ReactNode
10 | }) {
11 |   return (
12 |     <html lang="en">
13 |       <body>{children}</body>
14 |     </html>
15 |   )
16 | }
17 | 


--------------------------------------------------------------------------------
/web/src/components/ChatMessages/utils/createEmptyMessage.ts:
--------------------------------------------------------------------------------
 1 | import { v4 as uuidv4 } from "uuid";
 2 | import { type ChatMessage, type ChatMessageWithId } from "@langfuse/shared";
 3 | 
 4 | export function createEmptyMessage(message: ChatMessage): ChatMessageWithId {
 5 |   return {
 6 |     ...message,
 7 |     content: message.content ?? "",
 8 |     id: uuidv4(),
 9 |   };
10 | }
11 | 


--------------------------------------------------------------------------------
/web/src/components/editor/index.ts:
--------------------------------------------------------------------------------
1 | export * from "./CodeMirrorEditor";
2 | 


--------------------------------------------------------------------------------
/web/src/components/layouts/settings-table-card.tsx:
--------------------------------------------------------------------------------
 1 | import { Card } from "@/src/components/ui/card";
 2 | 
 3 | export const SettingsTableCard = ({
 4 |   children,
 5 | }: {
 6 |   children: React.ReactNode;
 7 | }) => {
 8 |   return (
 9 |     <Card className="mb-4 flex max-h-[60dvh] flex-col overflow-hidden [&>:first-child>:first-child]:border-t-0">
10 |       {children}
11 |     </Card>
12 |   );
13 | };
14 | 


--------------------------------------------------------------------------------
/web/src/components/layouts/spinner.tsx:
--------------------------------------------------------------------------------
 1 | import { LangfuseIcon } from "@/src/components/LangfuseLogo";
 2 | 
 3 | export function Spinner(props: { message: string }) {
 4 |   return (
 5 |     <div className="flex min-h-full flex-1 flex-col justify-center py-12 sm:px-6 lg:px-8">
 6 |       <div className="sm:mx-auto sm:w-full sm:max-w-md">
 7 |         <LangfuseIcon className="mx-auto motion-safe:animate-spin" size={42} />
 8 |         <h2 className="mt-5 text-center text-2xl font-bold leading-9 tracking-tight text-primary">
 9 |           {props.message} ...
10 |         </h2>
11 |       </div>
12 |     </div>
13 |   );
14 | }
15 | 


--------------------------------------------------------------------------------
/web/src/components/level-colors.tsx:
--------------------------------------------------------------------------------
 1 | import { type ObservationLevelType } from "@langfuse/shared";
 2 | 
 3 | export const LevelColors = {
 4 |   DEFAULT: { text: "", bg: "" },
 5 |   DEBUG: { text: "text-muted-foreground", bg: "bg-primary-foreground" },
 6 |   WARNING: { text: "text-dark-yellow", bg: "bg-light-yellow" },
 7 |   ERROR: { text: "text-dark-red", bg: "bg-light-red" },
 8 | };
 9 | 
10 | export const LevelSymbols = {
11 |   DEFAULT: "ℹ️",
12 |   DEBUG: "🔍",
13 |   WARNING: "⚠️",
14 |   ERROR: "🚨",
15 | };
16 | 
17 | export const formatAsLabel = (countLabel: string) => {
18 |   return countLabel.replace(/Count$/, "").toUpperCase() as ObservationLevelType;
19 | };
20 | 


--------------------------------------------------------------------------------
/web/src/components/table/peek/hooks/usePeekEvalConfigData.ts:
--------------------------------------------------------------------------------
 1 | import { api } from "@/src/utils/api";
 2 | 
 3 | type UsePeekEvalConfigDataProps = {
 4 |   projectId: string;
 5 |   jobConfigurationId?: string;
 6 | };
 7 | 
 8 | export const usePeekEvalConfigData = ({
 9 |   projectId,
10 |   jobConfigurationId,
11 | }: UsePeekEvalConfigDataProps) => {
12 |   return api.evals.configById.useQuery(
13 |     {
14 |       id: jobConfigurationId as string,
15 |       projectId,
16 |     },
17 |     {
18 |       enabled: !!jobConfigurationId,
19 |     },
20 |   );
21 | };
22 | 


--------------------------------------------------------------------------------
/web/src/components/table/peek/hooks/usePeekEvalTemplateData.ts:
--------------------------------------------------------------------------------
 1 | import { api } from "@/src/utils/api";
 2 | 
 3 | type UsePeekEvalTemplateDataProps = {
 4 |   projectId: string;
 5 |   templateId?: string;
 6 | };
 7 | 
 8 | export const usePeekEvalTemplateData = ({
 9 |   projectId,
10 |   templateId,
11 | }: UsePeekEvalTemplateDataProps) => {
12 |   return api.evals.templateById.useQuery(
13 |     {
14 |       id: templateId as string,
15 |       projectId,
16 |     },
17 |     {
18 |       enabled: !!templateId,
19 |     },
20 |   );
21 | };
22 | 


--------------------------------------------------------------------------------
/web/src/components/table/table-id.tsx:
--------------------------------------------------------------------------------
 1 | import { cn } from "@/src/utils/tailwind";
 2 | 
 3 | export default function TableIdOrName({
 4 |   value,
 5 |   className,
 6 | }: {
 7 |   value: string;
 8 |   className?: string;
 9 | }) {
10 |   return (
11 |     <div
12 |       title={value}
13 |       className={cn(
14 |         "inline-block max-w-full overflow-hidden text-ellipsis text-nowrap rounded py-0.5 text-xs font-semibold",
15 |         className,
16 |       )}
17 |     >
18 |       {value}
19 |     </div>
20 |   );
21 | }
22 | 


--------------------------------------------------------------------------------
/web/src/components/table/table-view-presets/hooks/useViewData.ts:
--------------------------------------------------------------------------------
 1 | import { api } from "@/src/utils/api";
 2 | 
 3 | type UseViewDataProps = {
 4 |   tableName: string;
 5 |   projectId: string;
 6 | };
 7 | 
 8 | export const useViewData = ({ tableName, projectId }: UseViewDataProps) => {
 9 |   const { data: TableViewPresets } =
10 |     api.TableViewPresets.getByTableName.useQuery({
11 |       tableName,
12 |       projectId,
13 |     });
14 | 
15 |   return {
16 |     TableViewPresetsList: TableViewPresets,
17 |   };
18 | };
19 | 


--------------------------------------------------------------------------------
/web/src/components/ui/collapsible.tsx:
--------------------------------------------------------------------------------
 1 | "use client";
 2 | 
 3 | import * as CollapsiblePrimitive from "@radix-ui/react-collapsible";
 4 | 
 5 | const Collapsible = CollapsiblePrimitive.Root;
 6 | 
 7 | const CollapsibleTrigger = CollapsiblePrimitive.CollapsibleTrigger;
 8 | 
 9 | const CollapsibleContent = CollapsiblePrimitive.CollapsibleContent;
10 | 
11 | export { Collapsible, CollapsibleTrigger, CollapsibleContent };
12 | 


--------------------------------------------------------------------------------
/web/src/components/ui/skeleton.tsx:
--------------------------------------------------------------------------------
 1 | import { cn } from "@/src/utils/tailwind";
 2 | 
 3 | function Skeleton({
 4 |   className,
 5 |   ...props
 6 | }: React.HTMLAttributes<HTMLDivElement>) {
 7 |   return (
 8 |     <div
 9 |       className={cn("animate-pulse rounded-md bg-muted", className)}
10 |       {...props}
11 |     />
12 |   );
13 | }
14 | 
15 | export { Skeleton };
16 | 


--------------------------------------------------------------------------------
/web/src/constants/VERSION.ts:
--------------------------------------------------------------------------------
1 | export const VERSION = "v3.68.0";
2 | 


--------------------------------------------------------------------------------
/web/src/constants/index.ts:
--------------------------------------------------------------------------------
1 | export { VERSION } from "./VERSION";
2 | 


--------------------------------------------------------------------------------
/web/src/ee/README.md:
--------------------------------------------------------------------------------
1 | # Enterprise Edition
2 | 
3 | This folder includes features that are only available in the Enterprise Edition of Langfuse and on Langfuse Cloud.
4 | 
5 | See [LICENSE](../../../LICENSE) and [docs](https://langfuse.com/docs/open-source) for more details.
6 | 


--------------------------------------------------------------------------------
/web/src/ee/features/billing/constants.ts:
--------------------------------------------------------------------------------
1 | export const MAX_EVENTS_FREE_PLAN = 50_000;
2 | 


--------------------------------------------------------------------------------
/web/src/ee/features/billing/utils/stripe.ts:
--------------------------------------------------------------------------------
1 | import { env } from "@/src/env.mjs";
2 | import Stripe from "stripe";
3 | 
4 | export const stripeClient =
5 |   env.STRIPE_SECRET_KEY && env.NEXT_PUBLIC_LANGFUSE_CLOUD_REGION
6 |     ? new Stripe(env.STRIPE_SECRET_KEY)
7 |     : undefined;
8 | 


--------------------------------------------------------------------------------
/web/src/ee/features/multi-tenant-sso/multiTenantSsoAvailable.ts:
--------------------------------------------------------------------------------
1 | import { env } from "@/src/env.mjs";
2 | 
3 | export const multiTenantSsoAvailable = Boolean(
4 |   env.NEXT_PUBLIC_LANGFUSE_CLOUD_REGION,
5 | );
6 | 


--------------------------------------------------------------------------------
/web/src/features/auth/hooks.ts:
--------------------------------------------------------------------------------
 1 | import { useSession } from "next-auth/react";
 2 | 
 3 | /**
 4 |  * Hook to check if the user is authenticated and a member of the project.
 5 |  */
 6 | export const useIsAuthenticatedAndProjectMember = (
 7 |   projectId: string,
 8 | ): boolean => {
 9 |   const session = useSession();
10 | 
11 |   if (projectId === "") return false;
12 | 
13 |   return (
14 |     session.status === "authenticated" &&
15 |     !!session.data?.user?.organizations
16 |       .flatMap((org) => org.projects)
17 |       .find(({ id }) => id === projectId)
18 |   );
19 | };
20 | 


--------------------------------------------------------------------------------
/web/src/features/auth/lib/projectNameSchema.ts:
--------------------------------------------------------------------------------
 1 | import { noHtmlCheck } from "@langfuse/shared";
 2 | import * as z from "zod/v4";
 3 | 
 4 | export const projectNameSchema = z.object({
 5 |   name: z
 6 |     .string()
 7 |     .min(3, "Must have at least 3 characters")
 8 |     .max(60, "Must have at most 60 characters")
 9 |     .refine((value) => noHtmlCheck(value), {
10 |       message: "Input should not contain HTML",
11 |     }),
12 | });
13 | 


--------------------------------------------------------------------------------
/web/src/features/auth/lib/projectRetentionSchema.ts:
--------------------------------------------------------------------------------
 1 | import * as z from "zod/v4";
 2 | 
 3 | export const projectRetentionSchema = z.object({
 4 |   retention: z.coerce
 5 |     .number()
 6 |     .int("Must be an integer")
 7 |     .refine((value) => value === 0 || value >= 3, {
 8 |       message: "Value must be 0 or at least 3 days",
 9 |     }),
10 | });
11 | 


--------------------------------------------------------------------------------
/web/src/features/batch-exports/README.md:
--------------------------------------------------------------------------------
1 | # Batch Exports
2 | 
3 | - Find types in shared
4 | - Actual export logic in worker
5 | 


--------------------------------------------------------------------------------
/web/src/features/cloud-status-notification/types.ts:
--------------------------------------------------------------------------------
1 | import { z } from "zod/v4";
2 | 
3 | export const CloudStatus = z
4 |   .enum(["operational", "downtime", "degraded", "maintenance"])
5 |   .nullable();
6 | 
7 | export type CloudStatus = z.infer<typeof CloudStatus>;
8 | 


--------------------------------------------------------------------------------
/web/src/features/dashboard/components/LeftAlignedCell.tsx:
--------------------------------------------------------------------------------
 1 | import { cn } from "@/src/utils/tailwind";
 2 | import { type ReactNode } from "react";
 3 | 
 4 | export const LeftAlignedCell = ({
 5 |   children,
 6 |   className,
 7 |   title,
 8 | }: {
 9 |   children: ReactNode;
10 |   className?: string;
11 |   title?: string;
12 | }) => (
13 |   <div className={cn("text-left", className)} title={title}>
14 |     {children}
15 |   </div>
16 | );
17 | 


--------------------------------------------------------------------------------
/web/src/features/dashboard/components/RightAlignedCell.tsx:
--------------------------------------------------------------------------------
 1 | import { cn } from "@/src/utils/tailwind";
 2 | import { type ReactNode } from "react";
 3 | 
 4 | export const RightAlignedCell = ({
 5 |   children,
 6 |   className,
 7 |   title,
 8 | }: {
 9 |   children: ReactNode;
10 |   className?: string;
11 |   title?: string;
12 | }) => (
13 |   <div className={cn("text-right", className)} title={title}>
14 |     {children}
15 |   </div>
16 | );
17 | 


--------------------------------------------------------------------------------
/web/src/features/evals/components/ragas-logo.tsx:
--------------------------------------------------------------------------------
 1 | export const RagasLogoIcon = () => {
 2 |   return (
 3 |     <div className="flex items-center">
 4 |       {/* eslint-disable-next-line @next/next/no-img-element */}
 5 |       <img
 6 |         src="/assets/ragas-logo.png"
 7 |         alt="Ragas Logo"
 8 |         width={12}
 9 |         height={12}
10 |       />
11 |     </div>
12 |   );
13 | };
14 | 


--------------------------------------------------------------------------------
/web/src/features/evals/hooks/useValidateCustomModel.ts:
--------------------------------------------------------------------------------
 1 | import { type ModelParams } from "@langfuse/shared";
 2 | 
 3 | export function useValidateCustomModel(
 4 |   availableProviders: string[],
 5 |   customModelParams?: {
 6 |     provider: string;
 7 |     model: string;
 8 |     modelParams: ModelParams & {
 9 |       maxTemperature: number;
10 |     };
11 |   },
12 | ): { isCustomModelValid: boolean } {
13 |   if (!customModelParams) {
14 |     return { isCustomModelValid: false };
15 |   }
16 | 
17 |   if (!availableProviders.includes(customModelParams.provider)) {
18 |     return { isCustomModelValid: false };
19 |   }
20 | 
21 |   return { isCustomModelValid: true };
22 | }
23 | 


--------------------------------------------------------------------------------
/web/src/features/feature-flags/README.md:
--------------------------------------------------------------------------------
 1 | # Feature Flags
 2 | 
 3 | Configure feature flags in the `available-flags.ts` file.
 4 | 
 5 | Use the `useIsFeatureEnabled` hook to check if a feature flag is enabled.
 6 | 
 7 | ```tsx
 8 | const isFeatureEnabled = useIsFeatureEnabled("feature-flag-name");
 9 | ```
10 | 
11 | When is a feature flag enabled?
12 | 
13 | 1. flag is in user.feature_flags
14 | 2. LANGFUSE_ENABLE_EXPERIMENTAL_FEATURES is set
15 | 3. user.admin is true
16 | 


--------------------------------------------------------------------------------
/web/src/features/feature-flags/available-flags.ts:
--------------------------------------------------------------------------------
1 | export const availableFlags = [
2 |   "templateFlag",
3 |   "excludeClickhouseRead",
4 | ] as const;
5 | 


--------------------------------------------------------------------------------
/web/src/features/feature-flags/hooks/useIsFeatureEnabled.ts:
--------------------------------------------------------------------------------
 1 | import { useSession } from "next-auth/react";
 2 | import type { Flag } from "../types";
 3 | 
 4 | export default function useIsFeatureEnabled(feature: Flag): boolean {
 5 |   const session = useSession();
 6 | 
 7 |   const isAdmin = session.data?.user?.admin ?? false;
 8 | 
 9 |   const isExperimentalFeaturesEnabled =
10 |     session.data?.environment.enableExperimentalFeatures ?? false;
11 | 
12 |   const isFeatureEnabledOnUser =
13 |     session.data?.user?.featureFlags[feature] ?? false;
14 | 
15 |   return isExperimentalFeaturesEnabled || isAdmin || isFeatureEnabledOnUser;
16 | }
17 | 


--------------------------------------------------------------------------------
/web/src/features/feature-flags/types.ts:
--------------------------------------------------------------------------------
1 | import { type availableFlags } from "./available-flags";
2 | 
3 | export type Flag = (typeof availableFlags)[number];
4 | export type Flags = {
5 |   [key in (typeof availableFlags)[number]]: boolean;
6 | };
7 | 


--------------------------------------------------------------------------------
/web/src/features/feature-flags/utils.ts:
--------------------------------------------------------------------------------
 1 | import { availableFlags } from "./available-flags";
 2 | import { type Flags } from "./types";
 3 | 
 4 | export const parseFlags = (dbFlags: string[]): Flags => {
 5 |   const parsedFlags = {} as Flags;
 6 | 
 7 |   availableFlags.forEach((flag) => {
 8 |     parsedFlags[flag] = dbFlags.includes(flag);
 9 |   });
10 | 
11 |   return parsedFlags;
12 | };
13 | 


--------------------------------------------------------------------------------
/web/src/features/models/components/ModelSettings.tsx:
--------------------------------------------------------------------------------
 1 | import Header from "@/src/components/layouts/header";
 2 | import ModelTable from "@/src/components/table/use-cases/models";
 3 | 
 4 | export function ModelsSettings(props: { projectId: string }) {
 5 |   return (
 6 |     <>
 7 |       <Header title="Models" />
 8 |       <p className="mb-2 text-sm">
 9 |         A model represents a LLM model. It is used to calculate tokens and cost.
10 |       </p>
11 |       <ModelTable projectId={props.projectId} />
12 |     </>
13 |   );
14 | }
15 | 


--------------------------------------------------------------------------------
/web/src/features/models/server/isValidPostgresRegex.ts:
--------------------------------------------------------------------------------
 1 | import { Prisma, type prisma as _prisma } from "@langfuse/shared/src/db";
 2 | 
 3 | export const isValidPostgresRegex = async (
 4 |   regex: string,
 5 |   prisma: typeof _prisma,
 6 | ): Promise<boolean> => {
 7 |   try {
 8 |     await prisma.$queryRaw(Prisma.sql`SELECT 'test_string' ~ ${regex}`);
 9 |     return true;
10 |   } catch {
11 |     return false;
12 |   }
13 | };
14 | 


--------------------------------------------------------------------------------
/web/src/features/models/utils.ts:
--------------------------------------------------------------------------------
 1 | import Decimal from "decimal.js";
 2 | 
 3 | export const getMaxDecimals = (
 4 |   value: number | undefined,
 5 |   scaleMultiplier: number = 1,
 6 | ) => {
 7 |   return (
 8 |     new Decimal(value ?? 0)
 9 |       .mul(scaleMultiplier)
10 |       .toFixed(12)
11 |       .split(".")[1]
12 |       ?.replace(/0+$/, "").length ?? 0
13 |   );
14 | };
15 | 


--------------------------------------------------------------------------------
/web/src/features/organizations/utils/organizationNameSchema.ts:
--------------------------------------------------------------------------------
 1 | import { noHtmlCheck } from "@langfuse/shared";
 2 | import * as z from "zod/v4";
 3 | 
 4 | export const organizationNameSchema = z.object({
 5 |   name: z
 6 |     .string()
 7 |     .min(3, "Must have at least 3 characters")
 8 |     .max(60, "Must have at most 60 characters")
 9 |     .refine((value) => noHtmlCheck(value), {
10 |       message: "Input should not contain HTML",
11 |     }),
12 | });
13 | 


--------------------------------------------------------------------------------
/web/src/features/playground/page/hooks/useCommandEnter.ts:
--------------------------------------------------------------------------------
 1 | import { useEffect } from "react";
 2 | 
 3 | export default function useCommandEnter(
 4 |   isEnabled: boolean,
 5 |   callback: () => Promise<void>,
 6 | ) {
 7 |   useEffect(() => {
 8 |     function handleKeyDown(event: KeyboardEvent) {
 9 |       if (
10 |         isEnabled &&
11 |         (event.metaKey || event.ctrlKey) &&
12 |         event.code === "Enter"
13 |       ) {
14 |         callback().catch((err) => console.error(err));
15 |       }
16 |     }
17 | 
18 |     document.addEventListener("keydown", handleKeyDown);
19 | 
20 |     return () => document.removeEventListener("keydown", handleKeyDown);
21 |   }, [isEnabled, callback]);
22 | }
23 | 


--------------------------------------------------------------------------------
/web/src/features/posthog-analytics/ServerPosthog.ts:
--------------------------------------------------------------------------------
 1 | import { env } from "@/src/env.mjs";
 2 | import { PostHog as OriginalPosthog } from "posthog-node";
 3 | 
 4 | // Safe as it is intended to be public
 5 | const PUBLIC_POSTHOG_API_KEY =
 6 |   env.NEXT_PUBLIC_POSTHOG_KEY ||
 7 |   "phc_zkMwFajk8ehObUlMth0D7DtPItFnxETi3lmSvyQDrwB";
 8 | const POSTHOG_HOST = env.NEXT_PUBLIC_POSTHOG_HOST || "https://eu.posthog.com";
 9 | 
10 | export class ServerPosthog extends OriginalPosthog {
11 |   constructor() {
12 |     super(PUBLIC_POSTHOG_API_KEY, {
13 |       host: POSTHOG_HOST,
14 |     });
15 | 
16 |     if (process.env.NODE_ENV === "development") this.debug();
17 |   }
18 | }
19 | 


--------------------------------------------------------------------------------
/web/src/features/posthog-integration/types.ts:
--------------------------------------------------------------------------------
 1 | import { z } from "zod/v4";
 2 | 
 3 | export const posthogIntegrationFormSchema = z.object({
 4 |   posthogHostname: z.string().url(),
 5 |   posthogProjectApiKey: z.string().refine((v) => v.startsWith("phc_"), {
 6 |     message:
 7 |       "PostHog 'Project API Key' must start with 'phc_'. You can find it in the PostHog project settings.",
 8 |   }),
 9 |   enabled: z.boolean(),
10 | });
11 | 


--------------------------------------------------------------------------------
/web/src/features/prompts/constants.ts:
--------------------------------------------------------------------------------
1 | export const PRODUCTION_LABEL = "production";
2 | export const LATEST_PROMPT_LABEL = "latest";
3 | export const COMMIT_MESSAGE_MAX_LENGTH = 500;
4 | 


--------------------------------------------------------------------------------
/web/src/features/prompts/utils.ts:
--------------------------------------------------------------------------------
1 | import {
2 |   LATEST_PROMPT_LABEL,
3 |   PRODUCTION_LABEL,
4 | } from "@/src/features/prompts/constants";
5 | 
6 | export const isReservedPromptLabel = (label: string) => {
7 |   return [PRODUCTION_LABEL, LATEST_PROMPT_LABEL].includes(label);
8 | };
9 | 


--------------------------------------------------------------------------------
/web/src/features/public-api/types/events.ts:
--------------------------------------------------------------------------------
1 | import { z } from "zod/v4";
2 | import { CreateEventEvent } from "@langfuse/shared/src/server";
3 | 
4 | // POST /events
5 | export const PostEventsV1Body = CreateEventEvent;
6 | export const PostEventsV1Response = z.object({ id: z.string() });
7 | 


--------------------------------------------------------------------------------
/web/src/features/public-api/types/generations.ts:
--------------------------------------------------------------------------------
 1 | // src/features/public-api/types/generations.ts
 2 | 
 3 | import { z } from "zod/v4";
 4 | import {
 5 |   LegacyGenerationsCreateSchema,
 6 |   LegacyGenerationPatchSchema,
 7 | } from "@langfuse/shared/src/server";
 8 | 
 9 | // POST /generations
10 | export const PostGenerationsV1Body = LegacyGenerationsCreateSchema;
11 | export const PostGenerationsV1Response = z.object({ id: z.string() });
12 | 
13 | // PATCH /generations
14 | export const PatchGenerationsV1Body = LegacyGenerationPatchSchema;
15 | export const PatchGenerationsV1Response = z.object({ id: z.string() });
16 | 


--------------------------------------------------------------------------------
/web/src/features/public-api/types/spans.ts:
--------------------------------------------------------------------------------
 1 | import { z } from "zod/v4";
 2 | import {
 3 |   LegacySpanPatchSchema,
 4 |   LegacySpanPostSchema,
 5 | } from "@langfuse/shared/src/server";
 6 | 
 7 | // POST /spans
 8 | export const PostSpansV1Body = LegacySpanPostSchema;
 9 | export const PostSpansV1Response = z.object({ id: z.string() });
10 | 
11 | // PATCH /spans
12 | export const PatchSpansV1Body = LegacySpanPatchSchema;
13 | export const PatchSpansV1Response = z.object({ id: z.string() });
14 | 


--------------------------------------------------------------------------------
/web/src/features/query/index.ts:
--------------------------------------------------------------------------------
1 | export * from "./dataModel";
2 | export * from "./dashboardUiTableToViewMapping";
3 | export * from "./types";
4 | 


--------------------------------------------------------------------------------
/web/src/features/rbac/constants/orderedRoles.ts:
--------------------------------------------------------------------------------
 1 | import { Role } from "@langfuse/shared";
 2 | 
 3 | export const orderedRoles: Record<Role, number> = {
 4 |   [Role.OWNER]: 4,
 5 |   [Role.ADMIN]: 3,
 6 |   [Role.MEMBER]: 2,
 7 |   [Role.VIEWER]: 1,
 8 |   [Role.NONE]: 0,
 9 | };
10 | 


--------------------------------------------------------------------------------
/web/src/features/scores/hooks/useScoreCustomOptimistic.ts:
--------------------------------------------------------------------------------
 1 | import { useCallback, useState } from "react";
 2 | 
 3 | export function useScoreCustomOptimistic<State, Action>(
 4 |   initialState: State,
 5 |   reducer: (state: State, action: Action) => State,
 6 | ): [State, (action: Action) => void] {
 7 |   const [state, setState] = useState<State>(initialState);
 8 | 
 9 |   const dispatch = useCallback(
10 |     (action: Action) => {
11 |       setState((currentState) => reducer(currentState, action));
12 |     },
13 |     [reducer],
14 |   );
15 | 
16 |   return [state, dispatch];
17 | }
18 | 


--------------------------------------------------------------------------------
/web/src/features/scores/schema.ts:
--------------------------------------------------------------------------------
 1 | import { ScoreDataType } from "@langfuse/shared";
 2 | import { z } from "zod/v4";
 3 | 
 4 | export const AnnotationScoreDataSchema = z.object({
 5 |   name: z.string(),
 6 |   scoreId: z.string().optional(),
 7 |   value: z.number().nullable().optional(),
 8 |   stringValue: z.string().optional(),
 9 |   dataType: z.enum(ScoreDataType),
10 |   configId: z.string().optional(),
11 |   comment: z.string().optional(),
12 | });
13 | 
14 | export const AnnotateFormSchema = z.object({
15 |   scoreData: z.array(AnnotationScoreDataSchema),
16 | });
17 | 


--------------------------------------------------------------------------------
/web/src/features/setup/setupRoutes.ts:
--------------------------------------------------------------------------------
 1 | export const createOrganizationRoute = "/setup";
 2 | 
 3 | export const createProjectRoute = (orgId: string) =>
 4 |   `/organization/${orgId}/setup?orgstep=create-project`;
 5 | 
 6 | export const inviteMembersRoute = (orgId: string) =>
 7 |   `/organization/${orgId}/setup?orgstep=invite-members`;
 8 | 
 9 | export const setupTracingRoute = (projectId: string) =>
10 |   `/project/${projectId}/setup`;
11 | 


--------------------------------------------------------------------------------
/web/src/features/slack/server/slack-webhook.ts:
--------------------------------------------------------------------------------
 1 | import { env } from "@/src/env.mjs";
 2 | 
 3 | export const sendToSlack = async (message: unknown) => {
 4 |   if (!env.LANGFUSE_TEAM_SLACK_WEBHOOK)
 5 |     throw new Error("LANGFUSE_TEAM_SLACK_WEBHOOK is not set");
 6 | 
 7 |   return await fetch(env.LANGFUSE_TEAM_SLACK_WEBHOOK, {
 8 |     method: "POST",
 9 |     body: JSON.stringify({ rawBody: JSON.stringify(message, null, 2) }),
10 |     headers: {
11 |       "Content-Type": "application/json",
12 |     },
13 |   });
14 | };
15 | 


--------------------------------------------------------------------------------
/web/src/features/support-chat/createSupportEmailHash.ts:
--------------------------------------------------------------------------------
 1 | import { env } from "@/src/env.mjs";
 2 | import { logger } from "@langfuse/shared/src/server";
 3 | import * as crypto from "node:crypto";
 4 | 
 5 | export const createSupportEmailHash = (email: string): string | undefined => {
 6 |   if (!env.PLAIN_AUTHENTICATION_SECRET) {
 7 |     if (env.NEXT_PUBLIC_LANGFUSE_CLOUD_REGION) {
 8 |       logger.error("PLAIN_AUTHENTICATION_SECRET is not set");
 9 |     }
10 |     return undefined;
11 |   }
12 |   const hmac = crypto.createHmac("sha256", env.PLAIN_AUTHENTICATION_SECRET);
13 |   hmac.update(email);
14 |   const hash = hmac.digest("hex");
15 |   return hash;
16 | };
17 | 


--------------------------------------------------------------------------------
/web/src/features/table/components/targetOptionsQueryMap.tsx:
--------------------------------------------------------------------------------
1 | import { api } from "@/src/utils/api";
2 | 
3 | export const targetOptionsQueryMap = {
4 |   "trace-add-to-annotation-queue": api.annotationQueues.allNamesAndIds.useQuery,
5 | } as const;
6 | 


--------------------------------------------------------------------------------
/web/src/features/table/server/helpers.ts:
--------------------------------------------------------------------------------
1 | export const generateBatchActionId = (
2 |   projectId: string,
3 |   actionId: string,
4 |   tableName: string,
5 | ) => {
6 |   return `${projectId}-${tableName}-${actionId}`;
7 | };
8 | 


--------------------------------------------------------------------------------
/web/src/features/telemetry/README.md:
--------------------------------------------------------------------------------
 1 | # Telemetry service for Docker deployments
 2 | 
 3 | By default, Langfuse automatically reports basic usage statistics to a centralized server (PostHog).
 4 | 
 5 | This helps us to:
 6 | 
 7 | 1. Understand how Langfuse is used and improve the most relevant features.
 8 | 2. Track overall usage for internal and external (e.g. fundraising) reporting.
 9 | 
10 | None of the data is shared with third parties and does not include any sensitive information. We want to be super transparent about this and you can find the exact data we collect [here](/src/features/telemetry/index.ts).
11 | 
12 | You can opt-out by setting `TELEMETRY_ENABLED=false`.
13 | 


--------------------------------------------------------------------------------
/web/src/features/theming/ThemeProvider.tsx:
--------------------------------------------------------------------------------
 1 | "use client";
 2 | 
 3 | import * as React from "react";
 4 | import { ThemeProvider as NextThemesProvider } from "next-themes";
 5 | import { type ThemeProviderProps } from "next-themes/dist/types";
 6 | 
 7 | export function ThemeProvider({ children, ...props }: ThemeProviderProps) {
 8 |   return <NextThemesProvider {...props}>{children}</NextThemesProvider>;
 9 | }
10 | 


--------------------------------------------------------------------------------
/web/src/features/widgets/chart-library/chart-props.ts:
--------------------------------------------------------------------------------
 1 | import { type ChartConfig } from "@/src/components/ui/chart";
 2 | 
 3 | export interface DataPoint {
 4 |   time_dimension: string | undefined;
 5 |   dimension: string | undefined;
 6 |   metric: number | Array<Array<number>>;
 7 | }
 8 | 
 9 | export interface ChartProps {
10 |   data: DataPoint[];
11 |   config?: ChartConfig;
12 |   accessibilityLayer?: boolean;
13 | }
14 | 


--------------------------------------------------------------------------------
/web/src/features/widgets/index.ts:
--------------------------------------------------------------------------------
1 | // Export the DataPoint type
2 | export { type DataPoint } from "./chart-library/chart-props";
3 | export { Chart } from "./chart-library/Chart";
4 | 
5 | // Export components
6 | export { WidgetForm } from "./components/WidgetForm";
7 | export { DashboardWidgetTable, DeleteWidget } from "./components/WidgetTable";
8 | export { DashboardWidget } from "./components/DashboardWidget";
9 | 


--------------------------------------------------------------------------------
/web/src/hooks/useProjectIdFromURL.ts:
--------------------------------------------------------------------------------
1 | import { useRouter } from "next/router";
2 | 
3 | export default function useProjectIdFromURL() {
4 |   const router = useRouter();
5 | 
6 |   return router.query.projectId as string | undefined;
7 | }
8 | 


--------------------------------------------------------------------------------
/web/src/instrumentation.ts:
--------------------------------------------------------------------------------
 1 | // See: https://vercel.com/docs/observability/otel-overview
 2 | export async function register() {
 3 |   // This variable is set in the .env file or environment variables
 4 |   // Value is true if NEXT_PUBLIC_LANGFUSE_RUN_NEXT_INIT is "true" or undefined
 5 |   const isInitLoadingEnabled =
 6 |     process.env.NEXT_PUBLIC_LANGFUSE_RUN_NEXT_INIT !== undefined
 7 |       ? process.env.NEXT_PUBLIC_LANGFUSE_RUN_NEXT_INIT === "true"
 8 |       : true;
 9 | 
10 |   if (process.env.NEXT_RUNTIME === "nodejs" && isInitLoadingEnabled) {
11 |     console.log("Running init scripts...");
12 |     await import("./observability.config");
13 |     await import("./initialize");
14 |   }
15 | }
16 | 


--------------------------------------------------------------------------------
/web/src/pages/api/auth/add-sso-config.ts:
--------------------------------------------------------------------------------
 1 | /**
 2 |  * This endpoint is used to add a new SSO configuration to the database.
 3 |  *
 4 |  * This is an EE feature and will return a 404 response if EE is not available.
 5 |  */
 6 | 
 7 | import { createNewSsoConfigHandler } from "@/src/ee/features/multi-tenant-sso/createNewSsoConfigHandler";
 8 | 
 9 | export default createNewSsoConfigHandler;
10 | 


--------------------------------------------------------------------------------
/web/src/pages/api/auth/signup.ts:
--------------------------------------------------------------------------------
1 | import { signupApiHandler } from "@/src/features/auth-credentials/server/signupApiHandler";
2 | 
3 | export default signupApiHandler;
4 | 


--------------------------------------------------------------------------------
/web/src/pages/api/billing/README.md:
--------------------------------------------------------------------------------
1 | These APIs are implemented via the NextJS App router in src/app/api/billing.
2 | 


--------------------------------------------------------------------------------
/web/src/pages/api/feedback.ts:
--------------------------------------------------------------------------------
1 | import feedbackApiHandler from "@/src/features/feedback/server/feedbackHandler";
2 | 
3 | export default feedbackApiHandler;
4 | 


--------------------------------------------------------------------------------
/web/src/pages/api/public/otel/otlp-proto/README.md:
--------------------------------------------------------------------------------
1 | # otlp-proto
2 | 
3 | This directory contains compiled opentelemetry protobuf files.
4 | Those should correspond to the definitions in https://github.com/open-telemetry/opentelemetry-proto/tree/v1.5.0 and are copied
5 | from the generated contents of https://www.npmjs.com/package/@opentelemetry/otlp-transformer.
6 | The file was converted from `.js` to `.ts` and the `export` statements were modified to make them Next.js compatible.
7 | 
8 | Unless there are relevant updates to the OpenTelemetry specification, there should be no need to ever touch this.
9 | 


--------------------------------------------------------------------------------
/web/src/pages/api/public/otel/v1/metrics/index.ts:
--------------------------------------------------------------------------------
 1 | import { withMiddlewares } from "@/src/features/public-api/server/withMiddlewares";
 2 | import { createAuthedProjectAPIRoute } from "@/src/features/public-api/server/createAuthedProjectAPIRoute";
 3 | import { z } from "zod/v4";
 4 | 
 5 | export const config = {
 6 |   api: {
 7 |     bodyParser: false,
 8 |   },
 9 | };
10 | 
11 | export default withMiddlewares({
12 |   POST: createAuthedProjectAPIRoute({
13 |     name: "OTel Metrics",
14 |     querySchema: z.any(),
15 |     responseSchema: z.any(),
16 |     rateLimitResource: "ingestion",
17 |     fn: async () => {},
18 |   }),
19 | });
20 | 


--------------------------------------------------------------------------------
/web/src/pages/api/public/v2/prompts/[promptName]/index.ts:
--------------------------------------------------------------------------------
1 | export { promptNameHandler as default } from "@/src/features/prompts/server/handlers/promptNameHandler";
2 | 


--------------------------------------------------------------------------------
/web/src/pages/api/public/v2/prompts/[promptName]/versions/[promptVersion].ts:
--------------------------------------------------------------------------------
1 | export { promptVersionHandler as default } from "@/src/features/prompts/server/handlers/promptVersionHandler";
2 | 


--------------------------------------------------------------------------------
/web/src/pages/api/public/v2/prompts/index.ts:
--------------------------------------------------------------------------------
1 | export { promptsHandler as default } from "@/src/features/prompts/server/handlers/promptsHandler";
2 | 


--------------------------------------------------------------------------------
/web/src/pages/auth/error.tsx:
--------------------------------------------------------------------------------
 1 | import { ErrorPageWithSentry } from "@/src/components/error-page";
 2 | import { useRouter } from "next/router";
 3 | 
 4 | export default function AuthError() {
 5 |   const router = useRouter();
 6 |   const { error } = router.query;
 7 |   const errorMessage = error
 8 |   ? decodeURIComponent(String(error))
 9 |     : "An authentication error occurred. Please reach out to support.";
10 | 
11 |   return (
12 |     <ErrorPageWithSentry title="Authentication Error" message={errorMessage} />
13 |   );
14 | }
15 | 


--------------------------------------------------------------------------------
/web/src/pages/background-migrations.tsx:
--------------------------------------------------------------------------------
1 | import BackgroundMigrationsTable from "@/src/features/background-migrations/components/background-migrations";
2 | 
3 | export default function BackgroundMigrationsPage() {
4 |   return <BackgroundMigrationsTable />;
5 | }
6 | 


--------------------------------------------------------------------------------
/web/src/pages/index.tsx:
--------------------------------------------------------------------------------
1 | import { OrganizationProjectOverview } from "@/src/features/organizations/components/ProjectOverview";
2 | 
3 | export default function Home() {
4 |   return <OrganizationProjectOverview />;
5 | }
6 | 


--------------------------------------------------------------------------------
/web/src/pages/organization/[organizationId]/index.tsx:
--------------------------------------------------------------------------------
1 | export { OrganizationProjectOverview as default } from "@/src/features/organizations/components/ProjectOverview";
2 | 


--------------------------------------------------------------------------------
/web/src/pages/organization/[organizationId]/settings/[page].tsx:
--------------------------------------------------------------------------------
1 | import OrgSettingsPage from "@/src/pages/organization/[organizationId]/settings";
2 | 
3 | export default OrgSettingsPage;
4 | 


--------------------------------------------------------------------------------
/web/src/pages/organization/[organizationId]/setup.tsx:
--------------------------------------------------------------------------------
1 | import { SetupPage } from "@/src/features/setup/components/SetupPage";
2 | 
3 | export default SetupPage;
4 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/annotation-queues.tsx:
--------------------------------------------------------------------------------
1 | import AnnotationQueues from "@/src/features/annotation-queues/pages/AnnotationQueues";
2 | 
3 | export default AnnotationQueues;
4 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/annotation-queues/[queueId]/index.tsx:
--------------------------------------------------------------------------------
1 | import QueueItems from "@/src/features/annotation-queues/pages/AnnotationQueueItems";
2 | 
3 | export default QueueItems;
4 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/annotation-queues/[queueId]/items/[itemId].tsx:
--------------------------------------------------------------------------------
 1 | import { AnnotationQueuesItem } from "@/src/features/annotation-queues/components/AnnotationQueuesItem";
 2 | import { useRouter } from "next/router";
 3 | 
 4 | export default function AnnotationQueues() {
 5 |   const router = useRouter();
 6 |   const annotationQueueId = router.query.queueId as string;
 7 |   const projectId = router.query.projectId as string;
 8 |   const itemId = router.query.itemId as string;
 9 | 
10 |   return (
11 |     <AnnotationQueuesItem
12 |       annotationQueueId={annotationQueueId}
13 |       projectId={projectId}
14 |       itemId={itemId}
15 |     />
16 |   );
17 | }
18 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/annotation-queues/[queueId]/items/index.tsx:
--------------------------------------------------------------------------------
 1 | import { AnnotationQueuesItem } from "@/src/features/annotation-queues/components/AnnotationQueuesItem";
 2 | import { useRouter } from "next/router";
 3 | 
 4 | export default function AnnotationQueues() {
 5 |   const router = useRouter();
 6 |   const annotationQueueId = router.query.queueId as string;
 7 |   const projectId = router.query.projectId as string;
 8 | 
 9 |   return (
10 |     <AnnotationQueuesItem
11 |       annotationQueueId={annotationQueueId}
12 |       projectId={projectId}
13 |     />
14 |   );
15 | }
16 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/evals/[evaluatorId].tsx:
--------------------------------------------------------------------------------
1 | import { EvaluatorDetail } from "@/src/features/evals/components/evaluator-detail";
2 | 
3 | export default EvaluatorDetail;
4 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/evals/default-model.tsx:
--------------------------------------------------------------------------------
1 | export { default as default } from "@/src/features/evals/pages/default-evaluation-model";
2 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/evals/index.tsx:
--------------------------------------------------------------------------------
1 | export { default as default } from "@/src/features/evals/pages/evaluators";
2 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/evals/new.tsx:
--------------------------------------------------------------------------------
1 | export { default as default } from "@/src/features/evals/pages/new-evaluator";
2 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/evals/templates/[id].tsx:
--------------------------------------------------------------------------------
1 | import { EvalTemplateDetail } from "@/src/features/evals/components/eval-template-detail";
2 | 
3 | export default EvalTemplateDetail;
4 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/evals/templates/index.tsx:
--------------------------------------------------------------------------------
1 | export { default as default } from "@/src/features/evals/pages/templates";
2 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/evals/templates/new.tsx:
--------------------------------------------------------------------------------
1 | export { default as default } from "@/src/features/evals/pages/new-template";
2 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/models.tsx:
--------------------------------------------------------------------------------
 1 | import { useRouter } from "next/router";
 2 | import { useEffect } from "react";
 3 | 
 4 | export default function ModelsPage() {
 5 |   const router = useRouter();
 6 |   const projectId = router.query.projectId as string;
 7 | 
 8 |   // temporarily redirect to settings/models
 9 |   useEffect(() => {
10 |     router.replace(`/project/${projectId}/settings/models`);
11 |   }, [projectId, router]);
12 | 
13 |   return null;
14 | }
15 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/playground.tsx:
--------------------------------------------------------------------------------
1 | export { default as default } from "@/src/features/playground/page";
2 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/prompts/[promptName]/index.tsx:
--------------------------------------------------------------------------------
1 | import { PromptDetail } from "@/src/features/prompts/components/prompt-detail";
2 | 
3 | export default PromptDetail;
4 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/prompts/new.tsx:
--------------------------------------------------------------------------------
1 | import { NewPrompt } from "@/src/features/prompts/components/prompt-new";
2 | 
3 | export default NewPrompt;
4 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/sessions/[sessionId].tsx:
--------------------------------------------------------------------------------
 1 | import { useRouter } from "next/router";
 2 | import { SessionPage } from "@/src/components/session";
 3 | 
 4 | export default function Trace() {
 5 |   const router = useRouter();
 6 |   const sessionId = router.query.sessionId as string;
 7 |   const projectId = router.query.projectId as string;
 8 | 
 9 |   return <SessionPage sessionId={sessionId} projectId={projectId} />;
10 | }
11 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/settings/[page].tsx:
--------------------------------------------------------------------------------
1 | import SettingsPage from "@/src/pages/project/[projectId]/settings";
2 | 
3 | export default SettingsPage;
4 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/settings/billing.ts:
--------------------------------------------------------------------------------
 1 | import { useQueryProject } from "@/src/features/projects/hooks";
 2 | import { useRouter } from "next/router";
 3 | import { useEffect } from "react";
 4 | 
 5 | export default function ProjectBillingRedirect() {
 6 |   const router = useRouter();
 7 | 
 8 |   const { organization } = useQueryProject();
 9 | 
10 |   useEffect(() => {
11 |     if (organization) {
12 |       router.replace(`/organization/${organization.id}/settings/billing`);
13 |     }
14 |   }, [organization, router]);
15 | 
16 |   return "Redirecting...";
17 | }
18 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/setup.tsx:
--------------------------------------------------------------------------------
1 | import { SetupPage } from "@/src/features/setup/components/SetupPage";
2 | 
3 | export default SetupPage;
4 | 


--------------------------------------------------------------------------------
/web/src/pages/project/[projectId]/traces/[traceId].tsx:
--------------------------------------------------------------------------------
 1 | import { TracePage } from "@/src/components/trace/TracePage";
 2 | import { useRouter } from "next/router";
 3 | 
 4 | export default function Trace() {
 5 |   const router = useRouter();
 6 |   const traceId = router.query.traceId as string;
 7 | 
 8 |   const timestamp =
 9 |     router.query.timestamp && typeof router.query.timestamp === "string"
10 |       ? new Date(decodeURIComponent(router.query.timestamp))
11 |       : undefined;
12 | 
13 |   return <TracePage traceId={traceId} timestamp={timestamp} />;
14 | }
15 | 


--------------------------------------------------------------------------------
/web/src/pages/public/traces/[traceId].tsx:
--------------------------------------------------------------------------------
 1 | // This url is deprecated, we keep this redirect page for backward compatibility
 2 | 
 3 | import TraceRedirectPage, {
 4 |   getServerSideProps,
 5 | } from "@/src/pages/trace/[traceId]";
 6 | 
 7 | export { getServerSideProps };
 8 | 
 9 | export default TraceRedirectPage;
10 | 


--------------------------------------------------------------------------------
/web/src/pages/setup.tsx:
--------------------------------------------------------------------------------
1 | import { SetupPage } from "@/src/features/setup/components/SetupPage";
2 | 
3 | export default SetupPage;
4 | 


--------------------------------------------------------------------------------
/web/src/server/api/definitions/evalExecutionsTable.ts:
--------------------------------------------------------------------------------
 1 | import { type ColumnDefinition, JobExecutionStatus } from "@langfuse/shared";
 2 | 
 3 | export const evalExecutionsFilterCols: ColumnDefinition[] = [
 4 |   {
 5 |     name: "Status",
 6 |     id: "status",
 7 |     type: "stringOptions",
 8 |     internal: 'je."status"::text',
 9 |     options: Object.values(JobExecutionStatus)
10 |       .filter((value) => value !== JobExecutionStatus.CANCELLED)
11 |       .map((value) => ({ value })),
12 |   },
13 | ];
14 | 


--------------------------------------------------------------------------------
/web/src/server/api/definitions/usersTable.ts:
--------------------------------------------------------------------------------
 1 | import { type ColumnDefinition } from "@langfuse/shared";
 2 | 
 3 | export const usersTableCols: ColumnDefinition[] = [
 4 |   {
 5 |     name: "Timestamp",
 6 |     id: "timestamp",
 7 |     type: "datetime",
 8 |     internal: 't."timestamp"',
 9 |   },
10 | ];
11 | 


--------------------------------------------------------------------------------
/web/src/server/api/routers/generations/index.ts:
--------------------------------------------------------------------------------
1 | import { createTRPCRouter } from "@/src/server/api/trpc";
2 | import { filterOptionsQuery } from "./filterOptionsQuery";
3 | import { getAllQueries } from "./getAllQueries";
4 | 
5 | export const generationsRouter = createTRPCRouter({
6 |   ...getAllQueries,
7 |   filterOptions: filterOptionsQuery,
8 | });
9 | 


--------------------------------------------------------------------------------
/web/src/server/api/routers/generations/utils/GenerationTableOptions.ts:
--------------------------------------------------------------------------------
 1 | import { z } from "zod/v4";
 2 | import { singleFilter, TracingSearchType } from "@langfuse/shared";
 3 | import { orderBy } from "@langfuse/shared";
 4 | 
 5 | export const GenerationTableOptions = z.object({
 6 |   projectId: z.string(), // Required for protectedProjectProcedure
 7 |   filter: z.array(singleFilter),
 8 |   searchQuery: z.string().nullable(),
 9 |   searchType: z.array(TracingSearchType),
10 |   orderBy: orderBy,
11 | });
12 | 


--------------------------------------------------------------------------------
/web/src/server/utils/checkProjectMembershipOrAdmin.ts:
--------------------------------------------------------------------------------
 1 | import { type User } from "next-auth";
 2 | 
 3 | export const isProjectMemberOrAdmin = (
 4 |   user: User | null | undefined,
 5 |   projectId: string,
 6 | ): boolean => {
 7 |   if (!user) return false;
 8 |   if (user.admin === true) return true;
 9 | 
10 |   const sessionProjects = user.organizations.flatMap((org) => org.projects);
11 |   const isProjectMember = sessionProjects.some(
12 |     (project) => project.id === projectId,
13 |   );
14 | 
15 |   return isProjectMember;
16 | };
17 | 


--------------------------------------------------------------------------------
/web/src/utils/exceptions.ts:
--------------------------------------------------------------------------------
 1 | import { Prisma } from "@langfuse/shared/src/db";
 2 | 
 3 | export function isPrismaException(e: unknown) {
 4 |   return (
 5 |     e instanceof Prisma.PrismaClientKnownRequestError ||
 6 |     e instanceof Prisma.PrismaClientUnknownRequestError ||
 7 |     e instanceof Prisma.PrismaClientRustPanicError ||
 8 |     e instanceof Prisma.PrismaClientInitializationError ||
 9 |     e instanceof Prisma.PrismaClientValidationError
10 |   );
11 | }
12 | 


--------------------------------------------------------------------------------
/web/src/utils/getFinalModelParams.tsx:
--------------------------------------------------------------------------------
 1 | import { type ModelParams, type UIModelParams } from "@langfuse/shared";
 2 | 
 3 | export function getFinalModelParams(modelParams: UIModelParams): ModelParams {
 4 |   return Object.entries(modelParams)
 5 |     .filter(([key, value]) => value.enabled && key !== "maxTemperature")
 6 |     .reduce(
 7 |       (params, [key, value]) => ({ ...params, [key]: value.value }),
 8 |       {} as ModelParams,
 9 |     );
10 | }
11 | 


--------------------------------------------------------------------------------
/web/src/utils/string.ts:
--------------------------------------------------------------------------------
 1 | export function lastCharacters(str: string, n: number) {
 2 |   return str.substring(str.length - n);
 3 | }
 4 | 
 5 | export function truncate(str: string, n: number = 16) {
 6 |   // '...' suffix if the string is longer than n
 7 |   if (str.length > n) {
 8 |     return str.substring(0, n) + "...";
 9 |   }
10 |   return str;
11 | }
12 | 


--------------------------------------------------------------------------------
/web/src/utils/superjson.ts:
--------------------------------------------------------------------------------
 1 | import Decimal from "decimal.js";
 2 | import { registerCustom } from "superjson";
 3 | 
 4 | export const setUpSuperjson = () => {
 5 |   registerCustom<Decimal, string>(
 6 |     {
 7 |       isApplicable: (v): v is Decimal => Decimal.isDecimal(v),
 8 |       serialize: (v) => v.toJSON(),
 9 |       deserialize: (v) => new Decimal(v),
10 |     },
11 |     "decimal.js",
12 |   );
13 | };
14 | 


--------------------------------------------------------------------------------
/web/src/utils/tailwind.ts:
--------------------------------------------------------------------------------
1 | import { clsx, type ClassValue } from "clsx";
2 | import { twMerge } from "tailwind-merge";
3 | 
4 | export function cn(...inputs: ClassValue[]) {
5 |   return twMerge(clsx(inputs));
6 | }
7 | 


--------------------------------------------------------------------------------
/web/tsconfig.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "extends": "@repo/typescript-config/nextjs.json",
 3 |   "compilerOptions": {
 4 |     "declaration": false,
 5 |     "declarationMap": false,
 6 |     "outDir": "dist",
 7 |     "plugins": [
 8 |       {
 9 |         "name": "next"
10 |       }
11 |     ],
12 |     "paths": {
13 |       "@/*": ["./*"]
14 |     },
15 |     "strictNullChecks": true
16 |   },
17 |   "exclude": ["node_modules", "sdk"],
18 |   "include": [
19 |     "src",
20 |     "next-env.d.ts",
21 |     ".next/types/**/*.ts",
22 |     ".eslintrc.js",
23 |     "next-env.d.ts",
24 |     "**/*.ts",
25 |     "**/*.tsx",
26 |     "**/*.cjs",
27 |     "**/*.mjs",
28 |     "types/global.d.ts"
29 |   ]
30 | }
31 | 


--------------------------------------------------------------------------------
/web/types/global.d.ts:
--------------------------------------------------------------------------------
1 | declare namespace JSX {
2 |   interface IntrinsicElements {
3 |     "stripe-pricing-table": React.DetailedHTMLProps<
4 |       React.HTMLAttributes<HTMLElement>,
5 |       HTMLElement
6 |     >;
7 |   }
8 | }
9 | 


--------------------------------------------------------------------------------
/worker/.eslintrc.js:
--------------------------------------------------------------------------------
 1 | /** @type {import("eslint").Linter.Config} */
 2 | module.exports = {
 3 |   extends: ["@repo/eslint-config/library.js"],
 4 |   parser: "@typescript-eslint/parser",
 5 |   parserOptions: {
 6 |     project: true,
 7 |   },
 8 |   ignorePatterns: ["**/*test*.*"],
 9 | };
10 | 


--------------------------------------------------------------------------------
/worker/src/backgroundMigrations/IBackgroundMigration.ts:
--------------------------------------------------------------------------------
1 | export interface IBackgroundMigration {
2 |   validate: (
3 |     args: Record<string, unknown>,
4 |   ) => Promise<{ valid: boolean; invalidReason: string | undefined }>;
5 |   run: (args: Record<string, unknown>) => Promise<void>;
6 |   abort: () => Promise<void>;
7 | }
8 | 


--------------------------------------------------------------------------------
/worker/src/constants/VERSION.ts:
--------------------------------------------------------------------------------
1 | export const VERSION = "v3.68.0";
2 | 


--------------------------------------------------------------------------------
/worker/src/database.ts:
--------------------------------------------------------------------------------
 1 | import { Kysely, PostgresDialect } from "kysely";
 2 | import { Pool } from "pg";
 3 | import { DB } from "@langfuse/shared";
 4 | import { env } from "./env";
 5 | 
 6 | export const db = new Kysely<DB>({
 7 |   dialect: new PostgresDialect({
 8 |     pool: new Pool({
 9 |       connectionString: env.DATABASE_URL,
10 |     }),
11 |   }),
12 | });
13 | 


--------------------------------------------------------------------------------
/worker/src/ee/cloudUsageMetering/constants.ts:
--------------------------------------------------------------------------------
1 | export const cloudUsageMeteringDbCronJobName = "cloud_usage_metering";
2 | 
3 | export enum CloudUsageMeteringDbCronJobStates {
4 |   Queued = "queued",
5 |   Processing = "processing",
6 | }
7 | 


--------------------------------------------------------------------------------
/worker/src/index.ts:
--------------------------------------------------------------------------------
1 | import "./instrumentation"; // instrumenting the application
2 | import app from "./app";
3 | import { env } from "./env";
4 | import { logger } from "@langfuse/shared/src/server";
5 | 
6 | export const server = app.listen(env.PORT, env.HOSTNAME, () => {
7 |   logger.info(`Listening: http://${env.HOSTNAME}:${env.PORT}`);
8 | });
9 | 


--------------------------------------------------------------------------------
/worker/src/initialize.ts:
--------------------------------------------------------------------------------
1 | import { upsertDefaultModelPrices } from "./scripts/upsertDefaultModelPrices";
2 | import { upsertManagedEvaluators } from "./scripts/upsertManagedEvaluators";
3 | import { upsertLangfuseDashboards } from "./scripts/upsertLangfuseDashboards";
4 | 
5 | upsertDefaultModelPrices();
6 | upsertManagedEvaluators();
7 | upsertLangfuseDashboards();
8 | 


--------------------------------------------------------------------------------
/worker/src/interfaces/ErrorResponse.ts:
--------------------------------------------------------------------------------
1 | import MessageResponse from "./MessageResponse";
2 | 
3 | export default interface ErrorResponse extends MessageResponse {
4 |   stack?: string;
5 | }
6 | 


--------------------------------------------------------------------------------
/worker/src/interfaces/MessageResponse.ts:
--------------------------------------------------------------------------------
1 | export default interface MessageResponse {
2 |   message: string;
3 | }
4 | 


--------------------------------------------------------------------------------
/worker/src/queues/scoreDelete.ts:
--------------------------------------------------------------------------------
 1 | import { Job, Processor } from "bullmq";
 2 | import { QueueName, TQueueJobTypes } from "@langfuse/shared/src/server";
 3 | 
 4 | import { processClickhouseScoreDelete } from "../features/scores/processClickhouseScoreDelete";
 5 | 
 6 | export const scoreDeleteProcessor: Processor = async (
 7 |   job: Job<TQueueJobTypes[QueueName.ScoreDelete]>,
 8 | ): Promise<void> => {
 9 |   const { scoreIds, projectId } = job.data.payload;
10 |   await processClickhouseScoreDelete(projectId, scoreIds);
11 | };
12 | 


--------------------------------------------------------------------------------
/worker/tsconfig.json:
--------------------------------------------------------------------------------
 1 | {
 2 |   "extends": "@repo/typescript-config/base.json",
 3 |   "compilerOptions": {
 4 |     "esModuleInterop": true,
 5 |     "module": "Node16",
 6 |     "moduleResolution": "Node16",
 7 |     "declaration": false,
 8 |     "declarationMap": false,
 9 |     "lib": ["ES2021"],
10 |     "outDir": "./dist",
11 |     "types": ["node"],
12 |     "downlevelIteration": true,
13 |     "resolveJsonModule": true
14 |   },
15 |   "include": ["."],
16 |   "exclude": ["node_modules", "dist", "src/**/*.test.ts"]
17 | }
18 | 


--------------------------------------------------------------------------------