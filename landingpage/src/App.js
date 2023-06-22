import logo from './logo.svg';
import './static/css/default.css';

/* import containers */
import Header from './Containers/Header';
import Navigation from './Containers/Navigation';
import { Features } from './Containers/Features';
import { Faq } from './Containers/Faq';
import { Conclutions } from './Containers/conclution';
import { Footer } from './Containers/Footer';
import { Beneficios } from './Containers/beneficios';



function App() {
  return (
    <>
    
      <Navigation />
      <Header />
      <Features />
      <Beneficios />
      <Faq />
      <Conclutions />
      <Footer />

    </>
  );
}

export default App;
