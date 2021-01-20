import axios from 'axios'

const getAPI = axios.create({
    //baseURL: 'http://127.0.0.1:5000',
    baseURL: 'https://ccdefaultapi.herokuapp.com/',
    timeout: 1000,
});

export {
    getAPI
}