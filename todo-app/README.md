# 📝 To-Do List Application

A modern, feature-rich to-do list application with local storage functionality. Built with vanilla JavaScript, HTML, and CSS.

## ✨ Features

### Core Features
- ✅ **Add Tasks** - Quickly add new tasks with Enter key support
- ✅ **Mark Complete** - Check off completed tasks with visual feedback
- ✅ **Delete Tasks** - Remove individual tasks
- ✅ **Local Storage** - All data persists in browser's localStorage
- ✅ **Filter Tasks** - View All, Active, or Completed tasks

### User Experience
- 📊 **Statistics** - Real-time count of total and completed tasks
- 🎨 **Beautiful UI** - Modern gradient design with smooth animations
- 📱 **Responsive Design** - Works perfectly on desktop and mobile devices
- ⚠️ **Input Validation** - Prevents adding empty tasks
- 🛡️ **XSS Protection** - HTML escaping for user input

### Advanced Features
- 🧹 **Clear Completed** - Remove all completed tasks at once
- ⏰ **Timestamps** - Each task shows creation date and time
- 💾 **Data Persistence** - Automatic saving to localStorage
- 📤 **Export/Import** - Save and load todos as JSON files (via API)

## 🚀 Quick Start

### 1. Open the Application
Simply open `index.html` in your web browser:
```bash
open todo-app/index.html
# or
firefox todo-app/index.html
# or
chrome todo-app/index.html
```

### 2. Add Your First Task
- Type a task in the input field
- Press Enter or click the "Add" button
- Your task appears in the list

### 3. Manage Tasks
- **Check** the checkbox to mark a task as complete
- **Click** Delete to remove a task
- **Use filters** to view specific task types

## 📖 Usage

### Adding Tasks
```
1. Type your task in the input field
2. Press Enter or click "Add"
3. Task is automatically saved to localStorage
```

### Filtering Tasks
- **All** - View all tasks
- **Active** - View only incomplete tasks
- **Completed** - View only completed tasks

### Clearing Tasks
- **Clear Completed** - Removes all completed tasks at once
- Click with confirmation to prevent accidental deletion

## 💾 Local Storage

The application uses browser's **localStorage** to persist data:
- **Storage Key**: `todoList`
- **Storage Format**: JSON array of todo objects
- **Persistence**: Data survives browser restart and tab closure
- **Browser Support**: All modern browsers (Chrome, Firefox, Safari, Edge)

### Todo Object Structure
```javascript
{
    id: 1234567890,              // Unique timestamp-based ID
    text: "Buy groceries",        // Task description
    completed: false,             // Completion status
    createdAt: "5/28/2026, 2:30:15 PM"  // Creation timestamp
}
```

## 🛠️ API Methods

The application exposes these methods through the global `app` object:

### Basic Operations
```javascript
app.addTodo()                   // Add a new todo
app.deleteTodo(id)              // Delete todo by ID
app.toggleTodo(id)              // Toggle completion status
app.clearCompleted()            // Clear all completed todos
```

### Filtering
```javascript
app.setFilter('all')            // Show all todos
app.setFilter('active')         // Show active todos
app.setFilter('completed')      // Show completed todos
app.getFilteredTodos()          // Get current filtered todos
```

### Data Management
```javascript
app.saveTodos()                 // Save todos to localStorage
app.loadTodos()                 // Load todos from localStorage
app.exportTodos()               // Export todos as JSON file
app.importTodos(file)           // Import todos from JSON file
app.clearAllTodos()             // Delete all todos
```

## 🎨 Customization

### Change Colors
Edit `styles.css` to modify:
- Primary gradient: `#667eea` and `#764ba2`
- Accent colors for buttons and highlights

### Change Storage Key
Edit `app.js`:
```javascript
this.storageKey = 'todoList';  // Change this value
```

### Add Custom Features
Extend the `TodoApp` class:
```javascript
// Add priority levels
priority: 'high' | 'medium' | 'low'

// Add due dates
dueDate: '2026-05-28'

// Add categories/tags
tags: ['work', 'personal']
```

## 📱 Browser Compatibility

| Browser | Support |
|---------|---------|
| Chrome  | ✅ Full |
| Firefox | ✅ Full |
| Safari  | ✅ Full |
| Edge    | ✅ Full |
| IE 11   | ⚠️ Partial |

## 💡 Tips & Tricks

1. **Keyboard Shortcut**: Press Enter to add tasks faster
2. **Quick Filtering**: Use filter buttons for quick navigation
3. **Backup Data**: Periodically export your todos as backup
4. **Mobile Friendly**: The app is fully responsive on mobile devices

## 📋 Example Usage

### Console API (for advanced users)
```javascript
// View all todos
console.log(app.todos);

// Get statistics
console.log(`Total: ${app.todos.length}`);
console.log(`Completed: ${app.todos.filter(t => t.completed).length}`);

// Programmatically add todo
app.todos.push({
    id: Date.now(),
    text: "New task",
    completed: false,
    createdAt: new Date().toLocaleString()
});
app.saveTodos();
app.render();
```

## 🐛 Troubleshooting

### Tasks Not Saving
- Check if localStorage is enabled in browser settings
- Clear browser cache and reload
- Try incognito/private mode to test

### Tasks Disappearing
- Check browser privacy/cookie settings
- localStorage has ~5-10MB limit per domain
- Clear old backups if storage is full

### App Not Loading
- Ensure all files (index.html, app.js, styles.css) are in same directory
- Check browser console for errors (F12)
- Try a different browser

## 📝 License

This project is open source and available for personal and commercial use.

## 🤝 Contributing

Feel free to fork, modify, and improve this application!

### Suggested Enhancements
- [ ] Add priority levels
- [ ] Add due dates and reminders
- [ ] Add categories/tags
- [ ] Add search functionality
- [ ] Add dark mode toggle
- [ ] Add edit functionality
- [ ] Add drag-and-drop reordering
- [ ] Add recurring tasks

---

**Made with ❤️ for productivity**
