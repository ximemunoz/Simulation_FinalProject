import { Box } from "@mui/material";
import Header from "../../components/Header";
import BarChart2021 from "../../components/BarChart2021";

const Bar2021 = () => {
  return (
    <Box m="20px">
      <Header title="Artist Revenue 2021" subtitle="Artist Share Distribution" />
      <Box height="75vh">
        <BarChart2021 />
      </Box>
    </Box>
  );
};

export default Bar2021;
