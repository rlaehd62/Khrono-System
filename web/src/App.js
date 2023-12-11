import Header from "./Header/init";
import Main from "./Main/init";
import Frame from "./Frame/init";

function App() {
  return (
    <Frame>
      <h1>{process.env.AAAA}</h1>
      <Header />
      <Main />
    </Frame>
  );
}

export default App;
