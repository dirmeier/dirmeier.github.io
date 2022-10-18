<template>
  <div class="container">
    <div class="columns">
      <div class="column is-12">
        <h3>Books</h3>
        <p>
          A list of books I've recently read to keep track
        </p>

        <table style=" width: 100%;">
          <thead>
            <tr>
              <th>Date</th>
              <th>Author</th>
              <th>Title</th>
              <th>Publisher</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="book in items" :key="book.title">
              <td style="min-width: 150px;">{{ book.date }}</td>
              <td style="min-width: 250px;">{{ book.author }}</td>
              <td style="min-width: 300px;">{{ book.title }}</td>
              <td style="min-width: 250px;">{{ book.publisher }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import books from "../assets/books.json";
export default {
  data: () => ({
    error: "",
    items: books
  })
};
</script>
