import React from 'react';
import './App.css';
import "antd/dist/antd.css";
import GetCategory from './components/getResult';
import { Layout, Input } from 'antd';

const { Footer, Content } = Layout;

function App() {
  return (
    <div className="App">
      <Layout>
        <Content>
          <GetCategory></GetCategory>
        </Content>
      </Layout>
    </div>
  );
}

export default App;
