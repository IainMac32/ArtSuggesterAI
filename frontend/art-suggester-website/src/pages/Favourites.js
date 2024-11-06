/*
 * Johann Caancan
 */
import "./Favourites.css"
import { useState } from "react";
import NavBar from "../components/NavBar";

export default function Favourites() {
    const [numFavs, setNumFavs] = useState(0);
    const [favourites, setFavorutites] = useState ([]);

    function addFav (){
        setNumFavs(numFavs + 1)
        const newFav = [...favourites, numFavs]
        setFavorutites(newFav)
    }

    return (
        <>
            <NavBar />
            <h2>Favourites Page</h2>
            <button onClick={() => {addFav()}}>Add Favourite</button>
            <div className="main">
            <ul className = 'favourites'>
            {favourites.map ((favItem, index) => {
                return (
                    <div className="favItem">
                        <li key = {index}>{favItem}</li>
                    </div>
                )
            }
                            )
            }
            </ul>
            </div>
            
            
        </>
    );
};