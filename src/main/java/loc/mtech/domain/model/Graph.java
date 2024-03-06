package loc.mtech.domain.model;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.util.List;

public class Graph {
    private static final Logger logger = LogManager.getLogger(Graph.class.getName());
    List<Edge> edges;
    List<Node> nodes;
}
