import { Box } from "@mui/material";
import Header from "../../components/Header";
import BarChart2022 from "../../components/BarChart2022";


const Bar2022 = () => {
  return (
    <Box m="20px">
      <Header title="Artist Revenue 2022" subtitle="Artist Share Distribution" />
      <Box height="75vh">
        <BarChart2022 />
      </Box>
    </Box>
  );
};

export default Bar2022;
