<template>
  <div class="container">
    <div align="center">
      <h2>Books</h2>
      <p style="font-size: 1.1em">
        A non-exhaustive list of books I've bought and read over the years.
      </p>
      <table>
        <thead>
          <tr>
            <th></th>
            <th>Author</th>
            <th>Title</th>
            <th>Publisher</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(entry, index) in messages" :key="index">
            <td style="min-width: 10px">{{ index + 1 }}</td>
            <td>{{ entry.author }}</td>
            <td>{{ entry.title }}</td>
            <td>{{ entry.publisher }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    error: "",
    messages: []
  }),
  mounted() {
    fetch("/get_books")
      .then(response => response.json())
      .then(result => {
        this.messages = result;
      });
  },
  methods: {}
};
</script>
