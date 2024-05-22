import { useTheme } from "@mui/material";
import { ResponsiveBar } from "@nivo/bar";
import { tokens } from "../theme";
import Data from "../data/DataOutput.json";

const BarChart2021 = ({ isDashboard = false }) => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const artistData = Data.GraphArtistas["2021"];
  const data = artistData.Band.map((band, index) => ({
    band: band,
    share: artistData.Share[index],
  }));

  return (
    <ResponsiveBar
      data={data}
      theme={{
  // added
  axis: {
    domain: {
      line: {
        stroke: colors.grey[100],
      },
    },
    legend: {
      text: {
        fill: colors.grey[100],
      },
    },
    ticks: {
      line: {
        stroke: colors.grey[100],
        strokeWidth: 1,
      },
      text: {
        fill: colors.grey[100],
      },
    },
  },
  legends: {
    text: {
      fill: colors.grey[100],
    },
  },
}}
      keys={["share"]}
      indexBy="band"
      margin={{ top: 50, right: 130, bottom: 50, left: 60 }}
      padding={0.3}
      valueScale={{ type: "linear" }}
      indexScale={{ type: "band", round: true }}
      colors={{ scheme: "nivo" }}
      borderColor={{
        from: "color",
        modifiers: [["darker", "1.6"]],
      }}
      axisTop={null}
      axisRight={null}
      axisBottom={{
        tickSize: 5,
        tickPadding: 5,
        tickRotation: 0,
        legend: isDashboard ? undefined : "Band",
        legendPosition: "middle",
        legendOffset: 32,
      }}
      axisLeft={{
        tickSize: 5,
        tickPadding: 5,
        tickRotation: 0,
        legend: isDashboard ? undefined : "Share",
        legendPosition: "middle",
        legendOffset: -40,
      }}
      enableLabel={false}
      labelSkipWidth={12}
      labelSkipHeight={12}
      labelTextColor={{
        from: "color",
        modifiers: [["darker", 1.6]],
      }}
      legends={[
        {
          dataFrom: "keys",
          anchor: "bottom-right",
          direction: "column",
          justify: false,
          translateX: 120,
          translateY: 0,
          itemsSpacing: 2,
          itemWidth: 100,
          itemHeight: 20,
          itemDirection: "left-to-right",
          itemOpacity: 0.85,
          symbolSize: 20,
          effects: [
            {
              on: "hover",
              style: {
                itemOpacity: 1,
              },
            },
          ],
        },
      ]}
      role="application"
      barAriaLabel={(e) => `${e.id}: ${e.formattedValue} in band: ${e.indexValue}`}
    />
  );
};

export default BarChart2021;

