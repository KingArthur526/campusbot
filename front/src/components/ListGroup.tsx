import { useState } from "react";


function ListGroup() {
  const items = [
    "Azerbaijan",
    "Turkey",
    "Armenia",
    "Los Santos",
    "Sandy Shores",
  ];
  const [selectedIndex, setSelectedIndex] = useState(-1)
  
  const message = items.length == 0 && <p> No items found</p>;
  return (
    <>
      <h1>List of Places</h1>
      {message}
      <ul className="list-group">
        {items.map((item, index) => (
          <li
            className= {selectedIndex === index ? 'list-group-item active' : 'list-group-item'}
            key={item}
            onClick={() => setSelectedIndex(index)}
          >
            {item}
          </li>
        ))}
      </ul>
    </>
  );
}

export default ListGroup;
