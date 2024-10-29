import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Login from './pages/Login';
import Favourites from './pages/Favourites';
import NoPage from './pages/NoPage';
import './App.css';
import "@fontsource/fira-code";
import CreateAccount from './pages/CreateAccount';

function App() {
  return (
    <div className="app-container">
      <BrowserRouter>
        <Routes>
          <Route index element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/favourites" element={<Favourites />} />
          <Route path = "/createAccount" element={<CreateAccount/>} />
          <Route path="*" element={<NoPage />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
