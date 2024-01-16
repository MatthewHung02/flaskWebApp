import React, {useState, useEffect} from "react";

function App(){
  const [data, setDate] = useState([{}])

  useEffect(() => {
    fetch("/charts").then(
      res => res.json()
    ).then(
      data => {
        setDate(data)
        console.log(data)
      }
    )

  },[]
  
  )

  return (
    
    <div>
     
    </div>

  )

}

export default App
