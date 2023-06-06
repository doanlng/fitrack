import React from "react";
import "./NavBar.css";
export default function NavBar() {
  const handleProgramsClick = async () => {
    try {
      const response = await fetch("http://localhost:8000/graphql", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          query: `
                        query {
                            allPrograms{
                                name
                            }
                        }
                    `,
        }),
      });
      const responseData = await response.json();
      console.log(responseData);
    } catch (error) {
      console.error("Error: ", error);
    }
  };
  return (
    <div className="NavBar">
      <p>Welcome to FitSync</p>
      <p>Home</p>
      <p>Workouts</p>
      <p onClick={handleProgramsClick}>Programs</p>
      <p>Profile</p>
    </div>
  );
}
