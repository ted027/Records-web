import React from 'react';
import ReactDOM from 'react-dom';
import {Provider} from 'react-redux';
import {createStore} from 'redux';
import todo from './reducers';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';

import { addTodo } from './actions';

let store = createStore(todo)

store.dispatch(addTodo('Helloooooo'))
console.log(store.getState())

ReactDOM.render(
    <Provider store={store}>
        <App />
    </Provider>,
    document.getElementById('root'));
registerServiceWorker();
