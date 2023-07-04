import './static/css/default.css';
import './static/css/team.css';

/* import containers */
import Header from './Containers/Header';
import Navigation from './Containers/Navigation';
import { Features } from './Containers/Features';
import { Faq } from './Containers/Faq';
import { Conclutions } from './Containers/conclution';
import { Footer } from './Containers/Footer';
import { Beneficios } from './Containers/beneficios';
import Examples from './Containers/screnshot';
import Team from './Containers/team';



function App() {
  return (
    <>
    
      <Navigation />
      <Header />
      <Features />
      <Examples />
      <Beneficios />
      <Faq />
      <Team/>
      <Conclutions />
      
      <Footer />

    </>
  );
}

export default App;
