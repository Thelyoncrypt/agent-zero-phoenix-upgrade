<!-- src/routes/+layout.svelte -->
<script>
    import AppHeader from '$lib/components/layout/AppHeader.svelte';
    import AppSidebar from '$lib/components/layout/AppSidebar.svelte';
    import AppInspectorPanel from '$lib/components/layout/AppInspectorPanel.svelte'; // NEW IMPORT
    import '$lib/styles/global.css'; // Global styles and CSS vars
    // Import stores for global initialization
    import { onMount } from 'svelte';
    import { socketStore } from '$lib/stores/socketStore.js';
    import { chatStore } from '$lib/stores/chatStore.js';

    let wsUrl = 'ws://localhost:8000/ws/agui'; // WebSocket URL for Agent Zero Phoenix
    let initialThreadId = `thread-${crypto.randomUUID().substring(0,8)}`;
    let initialUserId = `user-${crypto.randomUUID().substring(0,8)}`;

    onMount(() => {
        // Initialize chat store first
        chatStore.initializeSession(initialThreadId, initialUserId, "New Chat");

        // Connect socket store
        socketStore.connect(wsUrl, initialThreadId, initialUserId);

        // Wait for connection and then request chat list
        const unsubscribe = socketStore.subscribe(store => {
            if (store.isConnected) {
                chatStore.requestChatList();
                unsubscribe(); // Clean up listener
            }
        });
    });
</script>

<div class="app-container">
    <AppHeader />
    <div class="main-wrapper">
        <AppSidebar /> <!-- isOpen prop can be added for collapsibility -->
        
        <main class="main-content-area">
            <slot /> <!-- Page content (+page.svelte) goes here -->
        </main>

        <AppInspectorPanel /> <!-- ADDED: Right sidebar - isOpen prop for collapsibility -->
    </div>
</div>

<style>
    :global(body) { /* Apply to body for full page effect */
        margin: 0;
        background-color: var(--bg-dark-primary);
        color: var(--text-primary);
        font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
        overflow: hidden; /* Prevent body scroll, individual areas will scroll */
    }
    .app-container {
        display: flex;
        flex-direction: column;
        height: 100vh;
        max-height: 100vh; /* For iOS Safari */
    }
    .main-wrapper {
        display: flex;
        flex-grow: 1; /* Takes remaining vertical space */
        overflow: hidden; /* Crucial to contain children and enable their scrolling */
    }
    /* AppSidebar styles are in its own component or global */
    /* AppInspectorPanel styles are in its own component */

    .main-content-area {
        flex-grow: 1; /* This is the central column, it will take available space */
        display: flex; 
        flex-direction: column;
        overflow: hidden; /* Important for its child (.chat-layout-phoenix) to manage its own scroll */
        background-color: var(--bg-dark-primary); /* Ensure it has the base background */
    }
</style>
