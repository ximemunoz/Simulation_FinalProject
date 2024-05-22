import { Box, Typography, useTheme } from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";
import { tokens } from "../../theme";
import AdminPanelSettingsOutlinedIcon from "@mui/icons-material/AdminPanelSettingsOutlined";
import LockOpenOutlinedIcon from "@mui/icons-material/LockOpenOutlined";
import SecurityOutlinedIcon from "@mui/icons-material/SecurityOutlined";
import Header from "../../components/Header";
import Data from "../../data/DataOutput.json";

const Team = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  
  const columns = [
    {
      field: "Image",
      headerName: "Image",
      flex: 1,
      renderCell: (params) => (
        <img src={params.value} alt={params.row.Name} width="50" style={{ cursor: "pointer", borderRadius: "100%" }}/>
      )
    },
    { field: "Name", headerName: "Name", flex: 1, cellClassName: "name-column--cell" },
    { field: "Followers", headerName: "Followers", type: "number", width: 150 },
    { field: "followNew", headerName: "New Followers", type: "number", width: 150 },
    { field: "Popularity", headerName: "Popularity", type: "number", width: 120 },
    { field: "Level", headerName: "Level", type: "number", width: 100 },
    { field: "nivelNew", headerName: "New Level", type: "number", width: 100 },
    { field: "Growth", headerName: "Growth", type: "number", width: 100 },
    { 
      field: "Genres", 
      headerName: "Genres", 
      flex: 1, 
      renderCell: (params) => (
        <Typography>
          {params.value.join(", ")}
        </Typography>
      )
    },
    {
      field: "Url",
      headerName: "URL",
      flex: 1,
      renderCell: (params) => (
        <a href={params.value} target="_blank" rel="noopener noreferrer">
          {params.value}
        </a>
      )
    },
    
  ];

  // Extraer los datos de las bandas para el año 2023
  const rows = Data.GraphData["2023"].bands.map((band, index) => ({
    id: index,
    ...band,
  }));

  return (
    <Box m="20px">
      <Header title="ARTISTS" subtitle="Managing the Artists" />
      <Box
        m="40px 0 0 0"
        height="75vh"
        sx={{
          "& .MuiDataGrid-root": {
            border: "none",
          },
          "& .MuiDataGrid-cell": {
            borderBottom: "none",
          },
          "& .name-column--cell": {
            color: colors.greenAccent[300],
          },
          "& .MuiDataGrid-columnHeaders": {
            backgroundColor: colors.blueAccent[700],
            borderBottom: "none",
          },
          "& .MuiDataGrid-virtualScroller": {
            backgroundColor: colors.primary[400],
          },
          "& .MuiDataGrid-footerContainer": {
            borderTop: "none",
            backgroundColor: colors.blueAccent[700],
          },
          "& .MuiCheckbox-root": {
            color: `${colors.greenAccent[200]} !important`,
          },
        }}
      >
        <DataGrid checkboxSelection rows={rows} columns={columns} />
      </Box>
    </Box>
  );
};

export default Team;