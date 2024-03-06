package loc.mtech.domain.model;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.util.List;

public class Node {
    private static final Logger logger = LogManager.getLogger(Node.class.getName());
    int id;
    String name;
    List<Edge> edges;

    double x;
    double y;
}
