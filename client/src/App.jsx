import React, { useState } from 'react'
import axios from 'axios'

const App = () => {
  const [name , setName] = useState('')
   const handleClick = (e) => {
    axios.post('http://127.0.0.1:8000/user/message/' , {name}).then((res) => {
      console.log(res)
    })
   }
  return (
    <div>
      <input type="text" name="" id=""  onChange={(e) => setName(e.target.value)}/>
      <input type="button" value="Click" onClick={handleClick} />
    </div>
  )
}

export default App