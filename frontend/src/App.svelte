<script lang="ts">
  export let name_one: string = "Alice";
  export let name_two: string = "Bob";
  export let keywords: string = "red, green, blue";
  export let dialogue: { name: string; text: string }[] = [];
  export let fetching: boolean = false;

  const generate = async () => {
    console.log("fetching");
    fetching = true;
    const url = new URL("/generate", window.location.href);
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        accept: "application/json",
      },
      body: JSON.stringify({
        names: [name_one, name_two],
        keywords: keywords.split(",").map((s) => s.trim()),
      }),
    });
    const responseBody = await response.json();
    const dialogueStr: string = responseBody["dialogue"];
    dialogue = dialogueStr
      .split("\n")
      .filter((line) => line.trim().length > 0)
      .map((line) => line.split(":"))
      .map(([name, text]) => ({ name: name.trim(), text: text.trim() }));
    console.log("finished");
    fetching = false;
  };
</script>

<main>
  <h1 id="title">A.I.alogue</h1>
  <p class="description">
    Generate simple dialogues for learners of English as a second language that
    contain specific keywords.
  </p>
  <form>
    <label>Character names:</label>
    <input id="name-one" bind:value={name_one} />
    <input id="name-two" bind:value={name_two} />
    <label for="keywords">Keywords:</label>
    <input id="keywords" bind:value={keywords} />
  </form>
  {#if fetching}
    <p class="generating-info-box">Generating...</p>
  {:else}
    <button type="button" on:click={generate}>Generate!</button>
  {/if}
  <div class="dialogue">
    {#each dialogue as line}
      <p class="line"><b class="name">{line.name}:</b> {line.text}</p>
    {/each}
  </div>
  <footer>
    <p>
      Made by <a href="https://ha.nnes.dev/">Hannes</a>. Source code on
      <a href="https://github.com/hasnep/aialogue">GitHub</a>.
    </p>
  </footer>
</main>
