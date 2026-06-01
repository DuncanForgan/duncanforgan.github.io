<template>
  <div class="home">    
    <h1>Dr Duncan Forgan PhD</h1>

    <img
    width="400"
    src="../assets/Elevate-1521-crop.png"
    alt="A picture of Duncan.  He is wearing orange glasses, a pink shirt and a tweed blazer" />
    <p>Hi, I'm Duncan. I've been on a bit of a journey over my career.</p>    
    <p>I was a computational astrophysicist and astrobiologist for ten years, specialising in the formation of planets and the search for extraterrestrial intelligence (SETI).  You can find my book on the subject, <a href="https://www.cambridge.org/core/books/solving-fermis-paradox/46945FE622E1F62E8DA36832B9F58A8A">Solving Fermi's Paradox</a>, at all good bookstores.</p>
    <p>Since then, I've moved on into software engineering industry.  I'm now a Technical Lead at Dayshape, leading a team of engineers to improve the working lives of people in professional services.</p>
    <p>I'm a keen sci-fi writer and a member of the Edinburgh Science Fiction and Fantasy Discord (<a href="https://edinburghsff.com/">ESFF</a>)</p>
    <div class="nav-links">
      <router-link to="/blog" class="btn blog">Read My Blog Posts</router-link>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>


.nav-links {
  margin-top: 2rem;
}

.btn {
  display: inline-block;
  padding: 0.75rem 1.5rem;
  background-color: var(--nav-bar-color);
  color: white;
  text-decoration: none;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.btn:hover {
  background-color: var(--theme-primary);
}

</style>
