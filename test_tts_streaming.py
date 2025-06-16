#!/usr/bin/env python3
"""
Test script for ChatterboxTTSTool streaming functionality.
This script tests the TTS streaming with various text inputs.
"""

import asyncio
import os
import sys
import json
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from python.tools.chatterbox_tts_tool import ChatterboxTTSTool

async def test_tts_streaming():
    """Test the ChatterboxTTSTool with various text inputs."""
    
    print("🔊 Testing ChatterboxTTSTool Streaming Functionality")
    print("=" * 60)
    
    # Initialize the tool
    tool = ChatterboxTTSTool(
        agent_id="test_agent"
    )
    
    # Test scenarios
    test_scenarios = [
        {
            "name": "Short Text",
            "text": "Hello, this is a test of the text-to-speech system.",
            "description": "Test with a short, simple sentence"
        },
        {
            "name": "Medium Text",
            "text": "The ChatterboxTTSTool provides high-quality text-to-speech conversion with streaming capabilities. It can handle various types of text input and provides real-time audio output for immediate playback.",
            "description": "Test with a medium-length paragraph"
        },
        {
            "name": "Technical Text",
            "text": "Machine learning algorithms utilize neural networks to process data. The backpropagation algorithm adjusts weights and biases to minimize the loss function. This iterative process continues until convergence is achieved.",
            "description": "Test with technical terminology"
        },
        {
            "name": "Conversational Text",
            "text": "Hey there! How are you doing today? I hope you're having a great time testing this text-to-speech functionality. Let me know if you have any questions or if there's anything else I can help you with!",
            "description": "Test with conversational, friendly text"
        }
    ]
    
    for i, scenario in enumerate(test_scenarios, 1):
        print(f"\n🎤 Test {i}: {scenario['name']}")
        print(f"Description: {scenario['description']}")
        print(f"Text: '{scenario['text']}'")
        print("-" * 50)
        
        try:
            # Execute the TTS streaming
            result = await tool.execute(
                action="speak_streaming",
                text=scenario["text"],
                user_id="test_user",
                voice="default",
                speed=1.0,
                format="mp3"
            )
            
            if result.success:
                data = result.data
                print(f"✅ SUCCESS: {result.message}")
                print(f"🆔 Stream ID: {data.get('stream_id', 'N/A')}")
                print(f"🎵 Format: {data.get('format_hint', 'N/A')}")
                print(f"📊 Total chunks: {data.get('total_chunks', 'N/A')}")
                print(f"⏱️  Duration estimate: {data.get('duration_estimate', 'N/A')} seconds")
                
                # Check for any warnings or additional info
                if 'warnings' in data:
                    for warning in data['warnings']:
                        print(f"⚠️  Warning: {warning}")
                        
            else:
                print(f"❌ FAILED: {result.message}")
                if hasattr(result, 'error'):
                    print(f"Error: {result.error}")
                    
        except Exception as e:
            print(f"❌ EXCEPTION: {str(e)}")
            import traceback
            traceback.print_exc()
        
        print("\n" + "=" * 60)
    
    print("\n🏁 TTS Testing completed!")

async def test_error_scenarios():
    """Test error handling scenarios."""
    
    print("\n🧪 Testing TTS Error Scenarios")
    print("=" * 40)
    
    tool = ChatterboxTTSTool(agent_id="test_agent")
    
    # Test with empty text
    print("\n1. Testing empty text...")
    result = await tool.execute(action="speak_streaming", text="")
    print(f"Result: {'✅ PASS' if not result.success else '❌ FAIL'} - {result.message}")
    
    # Test with invalid action
    print("\n2. Testing invalid action...")
    result = await tool.execute(action="invalid_action", text="test")
    print(f"Result: {'✅ PASS' if not result.success else '❌ FAIL'} - {result.message}")
    
    # Test with very long text
    print("\n3. Testing very long text...")
    long_text = "This is a very long text. " * 1000  # 5000+ characters
    result = await tool.execute(action="speak_streaming", text=long_text)
    print(f"Result: {'✅ HANDLED' if result.success or 'too long' in result.message.lower() else '❌ UNEXPECTED'} - {result.message}")
    
    print("\n🏁 Error scenario testing completed!")

async def test_voice_options():
    """Test different voice options if available."""
    
    print("\n🎭 Testing Voice Options")
    print("=" * 30)
    
    tool = ChatterboxTTSTool(agent_id="test_agent")
    
    # Test different voices
    voices = ["default", "male", "female", "robotic"]
    test_text = "This is a test of different voice options."
    
    for voice in voices:
        print(f"\n🗣️  Testing voice: {voice}")
        try:
            result = await tool.execute(
                action="speak_streaming",
                text=test_text,
                voice=voice,
                speed=1.0
            )
            
            if result.success:
                print(f"✅ Voice '{voice}' supported")
                print(f"Stream ID: {result.data.get('stream_id', 'N/A')}")
            else:
                print(f"❌ Voice '{voice}' failed: {result.message}")
                
        except Exception as e:
            print(f"❌ Voice '{voice}' exception: {str(e)}")
    
    print("\n🏁 Voice testing completed!")

if __name__ == "__main__":
    # Run the tests
    asyncio.run(test_tts_streaming())
    asyncio.run(test_error_scenarios())
    asyncio.run(test_voice_options())
