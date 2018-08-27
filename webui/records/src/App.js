import React, { Component } from 'react';
// import logo from './logo.svg';
import './App.css';
import VisibleTodoList from './containers/VisibleTodoList';
import AddTodo from './containers/AddTodo';
import Filter from './components/Filter';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import AppBar from 'material-ui/AppBar';

class App extends Component {
  render() {
    return (
      <MuiThemeProvider>
      <div className="App">
        <AppBar
          title="TODO list"
          iconClassNameRight="muidocs-icon-navigation-expand-more"
        />
        <div>
          <AddTodo />
          <VisibleTodoList />
          <Filter />
        </div>
      </div>
      </MuiThemeProvider>
    );
  }
}

export default App;
