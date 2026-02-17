import React, { useState, useEffect } from "react";
import axios from "axios";

interface User {
  id: number;
  name: string;
  email: string;
}

interface FormData {
  name: string;
  email: string;
  password: string;
}

function App() {
  const [form, setForm] = useState<FormData>({
    name: "",
    email: "",
    password: "",
  });

  const [users, setUsers] = useState<User[]>([]);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const submitForm = async (e: React.FormEvent) => {
    e.preventDefault();

    await axios.post("http://127.0.0.1:8000/users", form);

    setForm({ name: "", email: "", password: "" });
    fetchUsers();
  };

  const fetchUsers = async () => {
    const res = await axios.get<User[]>("http://127.0.0.1:8000/users");
    setUsers(res.data);
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  return (
    <div style={{ padding: 40 }}>
      <h2>User Registration</h2>

      <form onSubmit={submitForm}>
        <input name="name" value={form.name} onChange={handleChange} placeholder="Name" /><br /><br />
        <input name="email" value={form.email} onChange={handleChange} placeholder="Email" /><br /><br />
        <input name="password" type="password" value={form.password} onChange={handleChange} placeholder="Password" /><br /><br />
        <button>Submit</button>
      </form>

      <h3>Users</h3>

      {users.map((u) => (
        <div key={u.id}>
          {u.name} — {u.email}
        </div>
      ))}
    </div>
  );
}

export default App;
