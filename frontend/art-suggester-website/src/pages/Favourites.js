/*
 * Johann Caancan
 */
import "./Favourites.css"
import { useState } from "react";
import NavBar from "../components/NavBar";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {faDownload, faStar } from '@fortawesome/free-solid-svg-icons'

export default function Favourites() {
    const [numFavs, setNumFavs] = useState(0);
    const [favourites, setFavorutites] = useState ([]);

    function addFav (){
        setNumFavs(numFavs + 1);
        const newFav = [...favourites, numFavs];
        setFavorutites(newFav);
    }

    function delFav(toDelIndex){
        const newFav = favourites.filter((favItem,favIndex) => favIndex !== toDelIndex);
        setFavorutites (newFav);

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
                    <div className="favItem" key = {index}>
                        {/*<li>{favItem}</li>*/}
                        <img src="/images/logo.png" alt="logo" className="img"/>
                        <div className="icons">
                            <FontAwesomeIcon icon={faDownload} className="download"/>
                            <FontAwesomeIcon icon={faStar} className="star" onClick={() => {delFav(index)}}/>
                        </div>
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