<script>
	import TodoList from './Components/TodoList.svelte';
	let todos = [{text: "Go to super", status: false}, {text: "Make food", status: true},{text: "Study", status: false}]
</script>

<main>
	<TodoList todos={todos}/>
</main>

<style>
</style>