<!-- src/routes/+page.svelte -->
<script>
    import { chatStore } from '$lib/stores/chatStore.js';
    import { socketStore } from '$lib/stores/socketStore.js';
    import MessageCard from '$lib/components/chat/MessageCard.svelte';
    import MessageInputBar from '$lib/components/chat/MessageInputBar.svelte';
    import StatusFooter from '$lib/components/chat/StatusFooter.svelte';
    import ToolCallCard from '$lib/components/chat/ToolCallCard.svelte';
    import AudioPlaybackControl from '$lib/components/chat/AudioPlaybackControl.svelte';
    import InspectorTabs from '$lib/components/inspector/InspectorTabs.svelte';

    let messageInputValue = '';

    function handleMessageSubmit(event) {
        const { text, attachments } = event.detail;

        if ((!text || !text.trim()) && (!attachments || attachments.length === 0)) return;
        if (!$socketStore.isConnected) return;

        // Create user message for display
        const userMessageForDisplay = {
            id: `msg-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`,
            role: 'user',
            content: text,
            timestamp: new Date().toISOString(),
            attachments: attachments || []
        };

        // Add to chat store
        chatStore.addMessage(userMessageForDisplay);

        // Create payload for Phoenix backend
        const payloadToPhoenix = {
            type: 'user_message',
            threadId: $chatStore.currentThreadId,
            userId: $chatStore.currentUserId,
            content: text,
            attachments: attachments || [],
            timestamp: new Date().toISOString()
        };

        // Send via WebSocket
        socketStore.sendMessage(payloadToPhoenix);
        messageInputValue = '';
    }
</script>

<!-- Split layout for testing InspectorTabs -->
<div class="chat-layout-phoenix">
    <div class="main-chat-area">
        <div class="chat-messages-container">
            {#each $chatStore.messagesAndEvents as item (item.id)}
                {#if item.type === 'message' || item.role}
                    <MessageCard message={item} />
                {:else if item.type === 'thought'}
                    <!-- ThoughtBubble will be added in later tasks -->
                    <div class="event-placeholder thought">
                        <strong>Thought:</strong> {item.content || item.text || JSON.stringify(item)}
                    </div>
                {:else if item.type === 'tool_call'}
                    <ToolCallCard toolCall={item} />
                {:else if item.type === 'error'}
                    <MessageCard message={{...item, role: 'error'}} />
                {:else}
                    <!-- Generic event display -->
                    <div class="event-placeholder generic">
                        <strong>{item.type}:</strong> {JSON.stringify(item)}
                    </div>
                {/if}
            {:else}
                <div class="no-messages">
                    <h3>🔥 Phoenix is ready</h3>
                    <p>Send a message to begin your conversation with Agent Zero Phoenix.</p>
                </div>
            {/each}
        </div>

        <!-- Audio Playback Control (appears when TTS is active) -->
        <AudioPlaybackControl />

        <MessageInputBar bind:inputValue={messageInputValue} on:send={handleMessageSubmit} disabled={!$socketStore.isConnected} />
        <StatusFooter />
    </div>

    <!-- Temporary Inspector Panel for testing TASK_AUI_003 -->
    <div class="inspector-test-panel">
        <InspectorTabs />
    </div>
</div>

<style>
    .chat-layout-phoenix {
        display: flex;
        flex-direction: row; /* Changed to row for split layout */
        flex-grow: 1; /* Fill the main-content-area from +layout.svelte */
        height: 100%; /* Ensure it tries to take full height of its flex parent */
        overflow: hidden; /* Important */
        background-color: var(--bg-dark-primary); /* Ensure this area has the base bg */
    }

    .main-chat-area {
        display: flex;
        flex-direction: column;
        flex: 1; /* Take remaining space */
        overflow: hidden;
    }

    .inspector-test-panel {
        width: 400px; /* Fixed width for testing */
        border-left: 1px solid var(--border-primary);
        background-color: var(--bg-dark-secondary);
        overflow: hidden;
        flex-shrink: 0;
    }

    .chat-messages-container {
        flex-grow: 1;
        overflow-y: auto;
        padding: 15px;
        display: flex;
        flex-direction: column;
        gap: 12px;
    }

    .chat-messages-container::-webkit-scrollbar {
        width: 8px;
    }

    .chat-messages-container::-webkit-scrollbar-track {
        background: var(--neumorphic-shadow-dark);
    }

    .chat-messages-container::-webkit-scrollbar-thumb {
        background-color: var(--accent-green-secondary);
        border-radius: 4px;
    }

    .no-messages {
        text-align: center;
        color: var(--text-secondary);
        margin-top: 20px;
        font-style: italic;
        padding: 40px 20px;
    }

    .no-messages h3 {
        color: var(--accent-green-primary);
        margin-bottom: 10px;
        font-size: 1.5em;
    }

    .event-placeholder {
        padding: 8px 12px;
        margin: 4px 0;
        border-radius: 8px;
        font-size: 0.9em;
        background-color: var(--bg-dark-secondary);
        border: 1px solid var(--border-primary);
        color: var(--text-secondary);
    }

    .event-placeholder.thought {
        border-left: 3px solid var(--accent-green-secondary);
    }

    .event-placeholder.tool-call {
        border-left: 3px solid var(--status-info);
    }

    .event-placeholder.generic {
        border-left: 3px solid var(--text-muted);
    }
</style>
