import axios from "axios";
import { useEffect, useState } from "react";
function App() {
  const [books, setBooks] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);
  useEffect(() => {
    setLoading(true);
    axios
      .get("books/list")
      .then((res) => {
        setLoading(true);
        setError(null);
        setBooks(res.data);
      })
      .catch((e) => {
        console.log(e);
      })
      .finally(() => setLoading(false));
  }, []);
  return (
    <div>
      {loading ? <p>Loading...</p> : null}
      {error ? <p>Error</p> : null}
      {books.length === 0 ? (
        <p>No books</p>
      ) : (
        <>
          {books.map((book) => (
            <p key={book.id}>{book.title}</p>
          ))}
        </>
      )}
    </div>
  );
}

export default App;
