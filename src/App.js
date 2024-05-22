import { useState } from "react";
import { Routes, Route } from "react-router-dom";
import Topbar from "./scenes/global/Topbar";
import Sidebar from "./scenes/global/Sidebar";
import Dashboard from "./scenes/dashboard";
import Team from "./scenes/team";
import Bar from "./scenes/bar";
import { CssBaseline, ThemeProvider } from "@mui/material";
import { ColorModeContext, useMode } from "./theme";
import Bar2021 from "./scenes/bar2021";
import Bar2022 from "./scenes/bar2022";

function App() {
  const [theme, colorMode] = useMode();
  const [isSidebar, setIsSidebar] = useState(true);

  return (
    <ColorModeContext.Provider value={colorMode}>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <div className="app">
          <Sidebar isSidebar={isSidebar} />
          <main className="content">
            <Topbar setIsSidebar={setIsSidebar} />
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/team" element={<Team />} />
              {/*<Route path="/contacts" element={<Contacts />} />*/}
              {/*<Route path="/invoices" element={<Invoices />} /> */}
              {/*<Route path="/form" element={<Form />} />*/}
              
              <Route path="/bar2021" element={<Bar2021 />} />
              <Route path="/bar2022" element={<Bar2022 />} />
              <Route path="/bar" element={<Bar />} />
              
              {/*<Route path="/faq" element={<FAQ />} />*/}
              {/*<Route path="/calendar" element={<Calendar />} />*/}
              
            </Routes>
          </main>
        </div>
      </ThemeProvider>
    </ColorModeContext.Provider>
  );
}

export default App;
