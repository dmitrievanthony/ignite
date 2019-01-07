package org.apache.ignite.ml.util;

import java.io.Serializable;
import java.util.function.Predicate;

public interface SerializablePredicate<T> extends Predicate<T>, Serializable {
}
