async function getGraphqlData() {
  //   console.log(JSON.stringify({ query }));
  const data = await fetch("https://graphql.country/graphql", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: '{"query":"{ countries { edges{node{name}} } }"}',
  });
  const responseData = await data.json();
  console.log(responseData.data.countries.edges);
}

getGraphqlData();
