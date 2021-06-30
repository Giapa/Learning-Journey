<script>
	import { scrapeIMDB } from "./Bot/bot"
	let name;
  let error = false;
  let loading = false;
	let cast = [];
	async function startBot(){
    if(name == null){
      error = true;
    } else {
      loading = true;
      scrapeIMDB(name);
      error = false;
      loading = false;
    }
	}
</script>

<main>
	<h1>Welcome to imdb bot</h1>
	<p>You can search any movie or series and I will return the cast using a bot</p>
	<input bind:value={name} type="text">
	<button on:click={()=> startBot()}>
		Return cast
	</button>
  {#if error}
     <br/><p>Name must not be empty</p>
  {/if}
  {#if loading}
     <br/><p>Loading... Please wait</p>
  {/if}
	<ul>
		{#each cast as actor}
			<li>{actor.name}</li>
		{/each}
	</ul>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}
	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}
	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>