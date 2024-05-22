import { Box, Button, IconButton, Typography, useTheme } from "@mui/material";
import { tokens } from "../../theme";
import Header from "../../components/Header";
import LineChart from "../../components/LineChart";
import BarChart2021 from "../../components/BarChart2021";
import BarChart2022 from "../../components/BarChart2022";
import BarChart from "../../components/BarChart";
import Data from"../../data/DataOutput.json";

const Dashboard = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const years = Object.keys(Data.GraphGrowth);

  return (
    <Box m="20px">
      
      {/* HEADER */}
      <Box display="flex" justifyContent="space-between" alignItems="center">
        <Header title="DASHBOARD" subtitle="Welcome to your dashboard" />

        <Box>
          
        </Box>
      </Box>

      {/* GRID & CHARTS */}
      <Box
        display="grid"
        gridTemplateColumns="repeat(12, 1fr)"
        gridAutoRows="140px"
        gap="20px"
      >
        

        {/* ROW 1 */}
        <Box
          gridColumn="span 5"
          gridRow="span 2"
          backgroundColor={colors.primary[400]}
        >
          <Box
            mt="25px"
            p="0 30px"
            display="flex "
            justifyContent="space-between"
            alignItems="center"
          >
            <Box>
            <Typography
                  variant="h5"
                  fontWeight="600"
                  color={colors.grey[100]}
                >
                  Artist Level Distribution:
                </Typography>
              
            </Box>
          </Box>
          <Box height="250px" m="-20px 0 0 0">
            <LineChart isDashboard={true} />
          </Box>
        </Box>
        <Box
          gridColumn="span 7"
          gridRow="span 2"
          backgroundColor={colors.primary[400]}
          overflow="auto"
        >
          <Box
            display="flex"
            justifyContent="space-between"
            alignItems="center"
            borderBottom={`4px solid ${colors.primary[500]}`}
            colors={colors.grey[100]}
            p="15px"
          >
            <Typography color={colors.grey[100]} variant="h5" fontWeight="600">
              Festival Growth
            </Typography>
          </Box>
          {years.map((year, i) => (
            <Box
              key={`${year}-${i}`}
              display="flex"
              justifyContent="space-between"
              alignItems="center"
              borderBottom={`4px solid ${colors.primary[500]}`}
              p="15px"
            >
              {/* AÑO BOX*/}
              <Box color={colors.grey[100]}>{year}</Box>
              {/* ASISTENTES BOX*/}
              <Box>
                <Typography
                  color={colors.greenAccent[500]}
                  variant="h5"
                  fontWeight="600"
                >
                  Attendants
                </Typography>
                <Typography color={colors.grey[100]}>
                  {Data.GraphGrowth[year].asistentes}
                </Typography>
              </Box>

              {/* PRECIO TICKET BOX*/}
              <Box>
                <Typography
                  color={colors.greenAccent[500]}
                  variant="h5"
                  fontWeight="600"
                >
                  Ticket Price:
                </Typography>
                <Typography color={colors.grey[100]}>
                  ${Data.GraphGrowth[year].tiketPrice}
                </Typography>
              </Box>

              {/* INGRESO TOTAL BOX*/}
              <Box>
                <Typography
                  color={colors.greenAccent[500]}
                  variant="h5"
                  fontWeight="600"
                >
                  Total Revenue:
                </Typography>
                <Typography color={colors.grey[100]}>
                  ${Data.GraphGrowth[year].ingreso} MDP
                </Typography>
              </Box>
              
              {/* % CRECIMIENTO BOX*/}
              <Box
                backgroundColor={colors.greenAccent[500]}
                p="5px 10px"
                borderRadius="4px"
              >
                {parseFloat(Data.GraphGrowth[year].porcentajeGrowth.toFixed(2))}%
              </Box>
              
            </Box>
          ))}
        </Box>
        <Box
          gridColumn="span 12"
          gridRow="span 3"
          backgroundColor={colors.primary[400]}
        >
         
          <Typography
                variant="h5"
                fontWeight="600"
                color={colors.grey[100]}
                sx={{ padding: "30px 30px 0 30px" }}
              >
                Total Revenue 2021:
              </Typography>
              <Typography
                variant="h3"
                fontWeight="bold"
                color={colors.greenAccent[500]}
                sx={{ padding: "0px 0px 0 30px" }}
              >
                ${Data.GraphGrowth[2021].ingreso} MDP
              </Typography>
          
          <Box height="300px" mt="-20px">
            <BarChart2021 isDashboard={true} />
          </Box>
        </Box>
        <Box
          gridColumn="span 12"
          gridRow="span 3"
          backgroundColor={colors.primary[400]}
        >
         
          <Typography
                variant="h5"
                fontWeight="600"
                color={colors.grey[100]}
                sx={{ padding: "30px 30px 0 30px" }}
              >
                Total Revenue 2022:
              </Typography>
              <Typography
                variant="h3"
                fontWeight="bold"
                color={colors.greenAccent[500]}
                sx={{ padding: "0px 0px 0 30px" }}
              >
                ${Data.GraphGrowth[2022].ingreso} MDP
              </Typography>
          
          <Box height="300px" mt="-20px">
            <BarChart2022 isDashboard={true} />
          </Box>
        </Box>
        <Box
          gridColumn="span 12"
          gridRow="span 3"
          backgroundColor={colors.primary[400]}
        >
         
          <Typography
                variant="h5"
                fontWeight="600"
                color={colors.grey[100]}
                sx={{ padding: "30px 30px 0 30px" }}
              >
                Total Revenue 2023:
              </Typography>
              <Typography
                variant="h3"
                fontWeight="bold"
                color={colors.greenAccent[500]}
                sx={{ padding: "0px 0px 0 30px" }}
              >
                ${Data.GraphGrowth[2023].ingreso} MDP
              </Typography>
          
          <Box height="300px" mt="-20px">
            <BarChart isDashboard={true} />
          </Box>
        </Box>
        
        

        {/* ROW 3 */}
        
        
      </Box>
      
      <Box>_</Box>
    </Box>
    
  );
};

export default Dashboard;
