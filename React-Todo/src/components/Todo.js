import React from "react";

const Todo = ({ text, todo, todos, setTodos }) => {
  const deleteHandler = (e) => {
    const item = e.target.parentElement;
    item.classList.add("fall");
    item.addEventListener("transitionend", () =>
      setTodos(todos.filter((el) => el.id !== todo.id))
    );
  };
  const completeHandler = () => {
    setTodos(
      todos.map((item) => {
        if (item.id === todo.id) {
          return {
            ...item,
            completed: !item.completed,
          };
        }
        return item;
      })
    );
  };
  return (
    <div className={`todo ${todo.completed ? "completed" : ""}`}>
      <li className="todo-item">{text}</li>
      <button onClick={completeHandler} className="completed-btn">
        <i className="fas fa-check"></i>
      </button>
      <button onClick={deleteHandler} className="deleted-btn">
        <i className="fas fa-trash"></i>
      </button>
    </div>
  );
};

export default Todo;
