package loc.mtech.domain.model;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class Edge {
    private static final Logger logger = LogManager.getLogger(Edge.class.getName());
    Node nodeA;
    Node nodeB;
    double length;
}
