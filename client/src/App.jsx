import React, { useEffect, useState } from 'react'
import axios from 'axios'
import { io } from "socket.io-client";
const App = () => {
  const [name , setName] = useState('')
  const socket = io("http://127.0.0.1:8000/car");
   const handleClick = (e) => {
    axios.post('http://127.0.0.1:8000/user/message/' , {name}).then((res) => {
      console.log(res)
    })
   }

   useEffect(() => {
    socket.on('message', (data) => {
      console.log(data.message);  // Update the state with the message received
    });

    // Clean up the socket connection when the component unmounts
    return () => {
      socket.off('message');
    };
  }, [socket]);

  return (
    <div>
      <input type="text" name="" id=""  onChange={(e) => setName(e.target.value)}/>
      <input type="button" value="Click" onClick={handleClick} />
    </div>
  )
}

export default App