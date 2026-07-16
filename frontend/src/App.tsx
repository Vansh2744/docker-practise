import axios from "axios";
import { useState } from "react";

function App() {
  const [user, setUser] = useState({
    name: "",
    email: "",
    username: "",
  });
  const getUser = async () => {
    const { data } = await axios.get("http://localhost:8000");
    setUser({
      name: data.name,
      email: data.email,
      username: data.username,
    });
  };
  getUser();
  return (
    <>
      <div>
        <h1>
          {user.name}
          {"  ||  "}
          <span>{user.username}</span>
        </h1>
        <h3>{user.email}</h3>
      </div>
    </>
  );
}

export default App;
