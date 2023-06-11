export default function MyApp() {
/*
la idea es que al apretar estos botones llamemos a componentes de react
que cambien el contenido de la pagina a la derecha del menu 
*/
    // una implementacion spa de la app
    function handleTrad() {
      alert("No funcional")
    return;
  }
    function handleJuego() {
	alert("No funcional")	
    return;
  }
    function handleProgre() {
	alert("No funcional")	
    return;
  }
    function handleSettings() {
	return <p class="normal">Test</p>;
  }    
    return (
	<>
	  <h2 class="normal">Bienvenido</h2>
	    <p class="normal">texto de bienvenida</p>
	  <div id="sidebar">
	    <div class="sidebar-header">
	      <h1>Menú</h1>
	    </div>
	    <ul class="sidebar-nav">
	      <li><Traduccion onClick={handleTrad} /></li>
	      <li><Juegos onClick={handleJuego} /></li>
	      <li><Progreso onClick={handleProgre} /></li>	    
	      <li><Settings onClick={handleSettings} /></li>
	    </ul>
	  </div>
	</>
    );
}

function Traduccion({ onClick }) {
    return (
    <button onClick={onClick}>
        Traduccion
    </button>
  );
}
function Juegos({ onClick }) {
    return (
    <button onClick={onClick}>
	Juegos
    </button>
  );    
}
function Progreso({ onClick }) {
    return (
    <button onClick={onClick}>
        Progreso
    </button>
  );    
}
function Settings({ onClick }) {
    return (
    <button onClick={onClick}>
        Settings
    </button>
  );    
}
