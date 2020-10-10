import React from 'react';
import logo from './logo.svg';
import './App.css';
import Elementos from './components/Elementos'
import Navegador from './components/navbar';

import 'bootstrap/dist/css/bootstrap.min.css';
import Grafica from './components/graficaram';
import GraficaCPU from './components/graficacpu';

function App() {
  return (
    <div className="App">
      <Navegador style={{"backgroundColor":"white"}}></Navegador>
      <header className="App-header">
      <Elementos></Elementos>
      <Grafica></Grafica>
      <hr></hr>
      <GraficaCPU></GraficaCPU>
      </header>
    </div>
  );
}

export default App;
