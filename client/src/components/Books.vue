<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Books</h1>
        <hr><br><br>
        <alert :message="message" v-if="showMessage"></alert>
        <v-btn depressed color="success" @click.stop="addBookModal = true">Add Book</v-btn>
        <br><br>
        <v-simple-table>
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Author</th>
              <th scope="col">Read?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(book, index) in books" :key="index">
              <td>{{ book.title }}</td>
              <td>{{ book.author }}</td>
              <td>
                <span v-if="book.read">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <v-container>
                  <v-btn
                    x-small depressed
                    color="warning"
                    @click="editBook(book)">
                    Update
                  </v-btn>
                  <v-btn
                    x-small depressed
                    color="error"
                    @click="onDeleteBook(book)">
                    Delete
                  </v-btn>
                </v-container>
              </td>
            </tr>
          </tbody>
        </v-simple-table>
      </div>
    </div>
    <v-dialog persistent v-model="addBookModal">
      <v-card>
        <v-card-title class="headline">Add Book</v-card-title>
          <v-card-text>
          <v-form @submit="onSubmit" @reset="onReset">
            <v-text-field
              v-model="addBookForm.title"
              label="Title:"
              placeholder="Enter title"
              required>
            </v-text-field>
            <v-text-field
              v-model="addBookForm.author"
              label="Author:"
              placeholder="Enter author"
              required>
            </v-text-field>
            <v-checkbox
              v-model="addBookForm.read"
              label="Read?"
              >
            </v-checkbox>
            <v-btn type="submit" color="primary">Submit</v-btn>
            <v-btn type="reset" color="error">Reset</v-btn>
          </v-form>
          </v-card-text>
        </v-card>
    </v-dialog>
  <v-dialog persistent v-model="editBookModal">
      <v-card>
        <v-card-title class="headline">Update Book</v-card-title>
          <v-card-text>
            <v-form @submit="onSubmitUpdate" @reset="onResetUpdate">
            <v-text-field
              v-model="editForm.title"
              label="Title:"
              placeholder="Enter title"
              required>
            </v-text-field>
            <v-text-field
              v-model="editForm.author"
              label="Author:"
              placeholder="Enter author"
              required>
            </v-text-field>
            <v-checkbox
              v-model="editForm.read"
              label="Read?"
              >
            </v-checkbox>
            <v-btn type="submit" color="primary">Update</v-btn>
            <v-btn type="reset" color="error">Cancel</v-btn>
          </v-form>
          </v-card-text>
        </v-card>
    </v-dialog>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      books: [],
      addBookModal: false,
      addBookForm: {
        title: '',
        author: '',
        read: false,
      },
      editBookModal: false,
      editForm: {
        id: '',
        title: '',
        author: '',
        read: false,
      },
      message: '',
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getBooks() {
      const path = 'http://localhost:5000/books';
      axios.get(path)
        .then((res) => {
          this.books = res.data.books;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addBook(payload) {
      const path = 'http://localhost:5000/books';
      axios.post(path, payload)
        .then(() => {
          this.getBooks();
          this.message = 'Book added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getBooks();
        });
    },
    editBook(book) {
      this.editForm = book;
      this.editBookModal = true;
    },
    updateBook(payload, bookID) {
      const path = `http://localhost:5000/books/${bookID}`;
      axios.put(path, payload)
        .then(() => {
          this.getBooks();
          this.message = 'Book updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks();
        });
    },
    initForm() {
      this.addBookForm.title = '';
      this.addBookForm.author = '';
      this.addBookForm.read = false;
      this.editForm.id = '';
      this.editForm.title = '';
      this.editForm.author = '';
      this.editForm.read = false;
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.addBookModal = false;
      const payload = {
        title: this.addBookForm.title,
        author: this.addBookForm.author,
        read: this.addBookForm.read, // property shorthand
      };
      this.addBook(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.addBookModal = false;
      this.initForm();
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.editBookModal = false;
      const payload = {
        title: this.editForm.title,
        author: this.editForm.author,
        read: this.editForm.read,
      };
      this.updateBook(payload, this.editForm.id);
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.editBookModal = false;
      this.initForm();
      this.getBooks();
    },
    removeBook(bookID) {
      const path = `http://localhost:5000/books/${bookID}`;
      axios.delete(path)
        .then(() => {
          this.getBooks();
          this.message = 'Book removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks();
        });
    },
    onDeleteBook(book) {
      this.removeBook(book.id);
    },
  },
  created() {
    this.getBooks();
  },
};
</script>
