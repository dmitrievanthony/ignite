package org.apache.ignite.ml.util;

import org.jetbrains.annotations.Nullable;

/** Logger. */
public interface TMPLogger {
    /**
     * Marker for log messages that are useful in development environments, but not in production.
     */
    String DEV_ONLY = "DEV_ONLY";

    /**
     * Creates new logger with given category based off the current instance.
     *
     * @param ctgr Category for new logger.
     * @return New logger with given category.
     */
    TMPLogger getLogger(Object ctgr);

    /**
     * Logs out trace message.
     *
     * @param msg Trace message.
     */
    void trace(String msg);

    /**
     * Logs out trace message.
     * The default implementation calls {@code this.trace(msg)}.
     *
     * @param marker Name of the marker to be associated with the message.
     * @param msg Trace message.
     */
    default void trace(@Nullable String marker, String msg) {
        trace(msg);
    }

    /**
     * Logs out debug message.
     *
     * @param msg Debug message.
     */
    void debug(String msg);

    /**
     * Logs out debug message.
     * The default implementation calls {@code this.debug(msg)}.
     *
     * @param marker Name of the marker to be associated with the message.
     * @param msg Debug message.
     */
    default void debug(@Nullable String marker, String msg) {
        debug(msg);
    }

    /**
     * Logs out information message.
     *
     * @param msg Information message.
     */
    void info(String msg);

    /**
     * Logs out information message.
     * The default implementation calls {@code this.info(msg)}.
     *
     * @param marker Name of the marker to be associated with the message.
     * @param msg Information message.
     */
    default void info(@Nullable String marker, String msg) {
        info(msg);
    }

    /**
     * Logs out warning message.
     *
     * @param msg Warning message.
     */
    default void warning(String msg) {
        warning(msg, null);
    }

    /**
     * Logs out warning message with optional exception.
     *
     * @param msg Warning message.
     * @param e Optional exception (can be {@code null}).
     */
    void warning(String msg, @Nullable Throwable e);

    /**
     * Logs out warning message with optional exception.
     * The default implementation calls {@code this.warning(msg)}.
     *
     * @param marker Name of the marker to be associated with the message.
     * @param msg Warning message.
     * @param e Optional exception (can be {@code null}).
     */
    default void warning(@Nullable String marker, String msg, @Nullable Throwable e) {
        warning(msg, e);
    }

    /**
     * Logs out error message.
     *
     * @param msg Error message.
     */
    default void error(String msg) {
        error(null, msg, null);
    }

    /**
     * Logs error message with optional exception.
     *
     * @param msg Error message.
     * @param e Optional exception (can be {@code null}).
     */
    void error(String msg, @Nullable Throwable e);

    /**
     * Logs error message with optional exception.
     * The default implementation calls {@code this.error(msg)}.
     *
     * @param marker Name of the marker to be associated with the message.
     * @param msg Error message.
     * @param e Optional exception (can be {@code null}).
     */
    default void error(@Nullable String marker, String msg, @Nullable Throwable e) {
        error(msg, e);
    }

    /**
     * Tests whether {@code trace} level is enabled.
     *
     * @return {@code true} in case when {@code trace} level is enabled, {@code false} otherwise.
     */
    boolean isTraceEnabled();

    /**
     * Tests whether {@code debug} level is enabled.
     *
     * @return {@code true} in case when {@code debug} level is enabled, {@code false} otherwise.
     */
    boolean isDebugEnabled();

    /**
     * Tests whether {@code info} level is enabled.
     *
     * @return {@code true} in case when {@code info} level is enabled, {@code false} otherwise.
     */
    boolean isInfoEnabled();

    /**
     * Tests whether Logger is in "Quiet mode".
     *
     * @return {@code true} "Quiet mode" is enabled, {@code false} otherwise
     */
    boolean isQuiet();

    /**
     * Gets name of the file being logged to if one is configured or {@code null} otherwise.
     *
     * @return Name of the file being logged to if one is configured or {@code null} otherwise.
     */
    String fileName();
}
