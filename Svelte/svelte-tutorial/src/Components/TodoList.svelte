<script>
    let text;
    export let todos;
    function toggleTodoStatus(index){
        todos[index].status = !todos[index].status;
    }
    function addTodo(){
        todos = [...todos, {text: text, status:false}]
        console.log(todos)
    }
    function removeTodo(todo){
        todos = todos.filter((item) => item !== todo)
    }
</script>
<style>
    .done {
        text-decoration: line-through;
    }
</style>
<div>
    <input bind:value={text} type="text">
    <button on:click={addTodo}>Add</button>
</div>
<ul>
{#each todos as todo, index}
  <li>
    <span on:click={()=> toggleTodoStatus(index)} class:done={todo.status}>{todo.text}</span>
    <span on:click={() => removeTodo(todo)}>❌</span>
  </li>
{/each}
</ul>
