package org.apache.ignite.ml.util;

import java.io.Serializable;
import java.util.Objects;
import org.jetbrains.annotations.Nullable;

/**
 * Convenience class representing mutable tuple of two values.
 */
public class BiTuple<V1, V2> implements Serializable {
    /** */
    private static final long serialVersionUID = -7257631915219950010L;

    /** First value. */
    private V1 val1;

    /** Second value. */
    private V2 val2;

    /**
     * Constructs a new instance of BiTuple.
     */
    public BiTuple() {
        // No-op.
    }

    /** Constructs a new instance of BiTuple using specified values. */
    public BiTuple(@Nullable V1 val1, @Nullable V2 val2) {
        this.val1 = val1;
        this.val2 = val2;
    }

    /** */
    public V1 get1() {
        return val1;
    }

    /** */
    public void set1(V1 val1) {
        this.val1 = val1;
    }

    /** */
    public V2 get2() {
        return val2;
    }

    /** */
    public void set2(V2 val2) {
        this.val2 = val2;
    }

    /** */
    public V1 getKey() {
        return val1;
    }

    /** */
    public V2 getValue() {
        return val2;
    }

    /** {@inheritDoc} */
    @Override public boolean equals(Object o) {
        if (this == o)
            return true;
        if (o == null || getClass() != o.getClass())
            return false;
        BiTuple<?, ?> tuple = (BiTuple<?, ?>)o;
        return Objects.equals(val1, tuple.val1) &&
            Objects.equals(val2, tuple.val2);
    }

    /** {@inheritDoc} */
    @Override public int hashCode() {
        return Objects.hash(val1, val2);
    }
}
