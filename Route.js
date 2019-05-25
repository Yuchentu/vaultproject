import Login from "./vaultima_project/Login";
import React from 'react';
import { Provider } from "react-redux";
import { BrowserRouter as Router, Route } from "react-router-dom";
import Root from "pages/Root"; 

const App = ({ }) => (
  <Provider store={store}>
    <Router>
      <Route path="/login" component={Login} />
    </Router>
  </Provider>
);

export default App;


