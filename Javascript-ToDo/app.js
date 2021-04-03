// Selectors
const todoInput = document.querySelector('.todo-input')
const todoButton = document.querySelector('.todo-button')
const todoList = document.querySelector('.todo-list')
const filterOption = document.querySelector('.filter-todos')

// Event listeners
document.addEventListener('DOMContentLoaded', getTodos);
todoButton.addEventListener('click', addTodo);
todoList.addEventListener('click', deleteCheck);
filterOption.addEventListener('click', filterTodo);

// Functions
function generateTodo(inputText, save=false) {
     // Todo div
     const todoDiv = document.createElement('div');
     todoDiv.classList.add('todo');
     // Create li
     const newTodo = document.createElement('li');
     newTodo.innerText = inputText;
     newTodo.classList.add('todo-item')
     todoDiv.appendChild(newTodo);
     // Add to storage
     if(save){
        saveLocalTodos(inputText);
     }
     // Add checkmark
     const completedButton = document.createElement('button');
     completedButton.innerHTML = '<i class="fas fa-check"></i>';
     completedButton.classList.add("completed-btn");
     todoDiv.appendChild(completedButton);
     // Add delete
     const deleteButton = document.createElement('button');
     deleteButton.innerHTML = '<i class="fas fa-trash"></i>';
     deleteButton.classList.add("deleted-btn");
     // Append buttons
     todoDiv.appendChild(deleteButton);
     todoList.appendChild(todoDiv);
}

function addTodo(event){
    event.preventDefault(); //Prevent form from submitting
    generateTodo(todoInput.value, true);
    todoInput.value = '';
}

function deleteCheck(event) {
    const item = event.target;
    // Delete
    if(item.classList[0] === 'deleted-btn') {
        const todo = item.parentElement;
        // Animation
        todo.classList.add('fall')
        todo.addEventListener('transitionend', (event) => event.target.remove());
        deleteLocalTodo(todo);
    }
    // Checked
    else if(item.classList[0] === 'completed-btn') {
        item.parentElement.classList.toggle("completed");
    }
}

function filterTodo(event) {
    const todos = todoList.childNodes;
    todos.forEach((todo) => {
        switch(event.target.value) {
            case "all":
                todo.style.display = 'flex';
                break;
            case "completed":
                if(todo.classList.contains('completed')){
                    todo.style.display = 'flex';
                } else {
                    todo.style.display = 'none';
                }
                break;
            case "uncompleted":
                if(!todo.classList.contains('completed')){
                    todo.style.display = 'flex';
                } else {
                    todo.style.display = 'none';
                }
                break;
        }
    });
}

function saveLocalTodos(todo){
    let todos = checkLocal();
    todos.push(todo);
    localStorage.setItem('todos', JSON.stringify(todos))
}

function deleteLocalTodo(todo){
    let todos = checkLocal();
    const todoText = todo.children[0].innerText;
    todos.splice(todos.indexOf(todoText),1);
    localStorage.setItem("todos", JSON.stringify(todos));
}

function getTodos(){
    let todos = checkLocal();
    todos.forEach(todo => generateTodo(todo));
}

function checkLocal(){
    let todos;
    if(localStorage.getItem('todos') === null){
        todos = [];
    } else {
        todos = JSON.parse(localStorage.getItem('todos'));
    }
    return todos;
}