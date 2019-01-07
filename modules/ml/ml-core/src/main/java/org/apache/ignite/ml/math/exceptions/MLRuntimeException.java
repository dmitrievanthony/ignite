package org.apache.ignite.ml.math.exceptions;

import org.jetbrains.annotations.Nullable;

/**
 * Base class for ML runtime exceptions.
 */
public class MLRuntimeException extends RuntimeException {
    /** */
    private static final long serialVersionUID = 7815048444590499591L;

    /**
     * Creates new exception with given error message.
     *
     * @param msg Error message.
     */
    public MLRuntimeException(String msg) {
        super(msg);
    }

    /**
     * Creates new grid exception with given throwable as a cause and
     * source of error message.
     *
     * @param cause Non-null throwable cause.
     */
    public MLRuntimeException(Throwable cause) {
        this(cause.getMessage(), cause);
    }

    /**
     * Creates new exception with given error message and optional nested exception.
     *
     * @param msg Error message.
     * @param cause Optional nested exception (can be {@code null}).
     */
    public MLRuntimeException(String msg, @Nullable Throwable cause) {
        super(msg, cause);
    }
}
