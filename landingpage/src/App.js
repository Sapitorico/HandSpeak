import logo from './logo.svg';
import './static/css/default.css';

import Header from './Containers/Header';
import Navigation from './Containers/Navigation';
import { Features } from './Containers/Features';
import { Faq } from './Containers/Faq';
import { Conclutions } from './Containers/conclution';
import { Footer } from './Containers/Footer';


function App() {
  return (
    <>
    
      <Navigation />
      <Header />
      <Features />
      <Faq />
      <Conclutions />
      <Footer />

    </>
  );
}

export default App;
