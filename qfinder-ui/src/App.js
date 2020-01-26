import React from 'react';
import './App.css';
import "antd/dist/antd.css";
import GetCategory from './components/getResult';
import { Layout, Input } from 'antd';

const { Header, Footer, Sider, Content } = Layout;

function App() {
  return (
    <div className="App">
      <Layout>
        <Layout>
          <GetCategory></GetCategory>
        </Layout>
      </Layout>
    </div>
  );
}

export default App;
