import Vue from 'vue';
import VueRouter from 'vue-router';
import Prediction from './views/Prediction';
import Article from './views/Article';

Vue.use(VueRouter)

export default new VueRouter({
    mode:'history',
    routes:[{
            path: '/',
            name: 'prediction',
            component: Prediction
        },{
            path: '/article',
            name: 'article',
            component: Article
        }, 
    ],
});