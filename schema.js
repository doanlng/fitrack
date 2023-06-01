const graphql = require("graphql");
const {
  GraphQLObjectType,
  GraphQLString,
  GraphQLSchema,
  GraphQLID,
  GraphQLInt,
  GraphQLList,
  GraphQLNonNull,
} = graphql;

const ExerciseType = new GraphQLObjectType({
  name: "Exercise",
  fields: () => ({
    name: { type: GraphQLString },
    exercise_type: { type: GraphQLString },
  }),
});

const RootQuery = new GraphQLObjectType({
  name: "RootQueryType",
  fields: {
    exercise: {
      type: ExerciseType,
      args: { name: { type: GraphQLString } },
      resolve(parent, args) {
        // code to get data from db / other source
      },
    },
  },
});

module.exports = new GraphQLSchema({
  query: RootQuery,
});
